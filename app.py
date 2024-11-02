import gradio as gr
from graph import graph  
import uuid
from langchain_core.messages import HumanMessage

random_id = uuid.uuid4()
print("Random ID: ", random_id)


def chatbot_response(input_text, history):
    thread = {"configurable": {"thread_id": random_id}}
    messages = [HumanMessage(content=input_text)]

    output_text = graph.invoke({'messages': messages}, config=thread)

    return output_text['messages'][-1].content


gr.ChatInterface(
    chatbot_response,
    type="messages",
    textbox=gr.Textbox(),
    title="Wellbeing Companion",
    description="Share your thoughts and feelings in a safe, supportive space.",
    theme="soft",
    cache_examples=True
).launch()

