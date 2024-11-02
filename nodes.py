import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, RemoveMessage
from langgraph.graph import END
from langchain_community.tools import TavilySearchResults

from prompts import ASSISTANT_PROMPT, LISTENER_PROMPT, RESULTS_ANALYSIS_PROMPT, SEARCH_QUERY_PROMPT
from schemas import ActiveListener, HealthAdvisor

load_dotenv()
llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), temperature=0.4, model='gpt-4o-mini')
search = TavilySearchResults(max_results=2)


def listener(state):
    listener_notes = llm.with_structured_output(ActiveListener).invoke([SystemMessage(content=LISTENER_PROMPT)] + state['messages'])
    return {"listener_notes": listener_notes, "expert_solutions": {}}


def assistant(state):
    summary = state.get("summary", "")

    listener_notes = state['listener_notes']
    expert_solutions = state['expert_solutions'] if state['expert_solutions'] != {} else {}
    condition = state['expert_solutions'].condition if state['expert_solutions'] != {} else ""
    solutions = state['expert_solutions'].solutions if state['expert_solutions'] != {} else ""


    print("Listener Notes: ", listener_notes)
    print("Expert Solutions: ", expert_solutions)
    
    response = llm.invoke([SystemMessage(content=ASSISTANT_PROMPT.format(key_issues=listener_notes.key_issues, 
                                                                        root_cause=listener_notes.root_cause,
                                                                        online_medical_citation=listener_notes.check_online_medical_citations,
                                                                        condition=condition,
                                                                        solutions=solutions,
                                                                        summary=summary
                                                                        ))] + state['messages'])

    return {'messages': response}


def web_search_solution(state):
    query = llm.invoke([SystemMessage(content=SEARCH_QUERY_PROMPT)] + state['messages'])

    search_docs = search.invoke(query.content)

    final_results = llm.with_structured_output(HealthAdvisor).invoke([SystemMessage(content=RESULTS_ANALYSIS_PROMPT.format(
        search_docs=search_docs
    ))] + state['messages'])

    return {"expert_solutions": final_results}


def decide_to_provide_solution(state):
    if state['listener_notes'].check_online_medical_citations == True:
        return "health_advisor_agent"
    else:
        return "assistant_agent"
    

def summarize_conversation(state):
    summary = state.get("summary", "")

    if summary:
        summary_message = (
            f"This is a summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into action the new messages above."
            "Ensure the summary keeps on capturing the main points of discussion while still emphasizing the key issues affecting the client, as these will guide the assistant's future responses."
            "It should be clear and conscise."
        )
        messages = state['messages'] + [HumanMessage(content=summary_message.format(summary=summary))]

    else:
        summary_message = """
            Summarize the conversation so far, keeping in mind the client's core issues, emotional state, and any recurring themes or concerns they have expressed. 
            Ensure the summary captures the main points of discussion while emphasizing the key issues affecting the client, as these will guide the assistant's future responses. 
            This summary should be clear, concise, and suitable for use in ongoing supportive and empathetic guidance.
        """
        messages = state['messages'] + [HumanMessage(content=summary_message)]

    summary_response = llm.invoke(messages)

    delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
    return {"summary": summary_response.content, "messages": delete_messages}


def should_summarize(state):
    messages = state["messages"]

    if len(messages) > 4:
        return "summarization_agent"
    else:
        return END
