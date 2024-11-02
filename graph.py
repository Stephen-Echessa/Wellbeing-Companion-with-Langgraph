from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.sqlite import SqliteSaver
from schemas import AssistantState
from nodes import assistant, listener, web_search_solution, decide_to_provide_solution, summarize_conversation, should_summarize

import sqlite3 

conn = sqlite3.connect(database=':memory' , check_same_thread=False)
memory = SqliteSaver(conn=conn)

builder = StateGraph(AssistantState)

builder.add_node("listener_agent", listener)
builder.add_node("assistant_agent", assistant)
builder.add_node("summarization_agent", summarize_conversation)
builder.add_node("health_advisor_agent", web_search_solution)

builder.add_edge(START, "listener_agent")
builder.add_conditional_edges("listener_agent", decide_to_provide_solution, ["health_advisor_agent", "assistant_agent"])
builder.add_edge("health_advisor_agent", "assistant_agent")
builder.add_conditional_edges("assistant_agent", should_summarize, ["summarization_agent", END])
builder.add_edge("summarization_agent", END)

graph = builder.compile(memory)