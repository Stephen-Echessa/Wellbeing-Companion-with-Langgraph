import streamlit as st
from graph import graph  
import uuid
from langchain_core.messages import HumanMessage

st.title("Wellbeing Companion")
st.subheader("Share your thoughts and feelings in a safe, supportive space")

# Initialize session state for unique ID and chat history
if "user_id" not in st.session_state:
    st.session_state.user_id = uuid.uuid4()

if "messages" not in st.session_state:
    st.session_state.messages = []


# Function to handle chatbot responses
def chatbot_response(input_text):
    thread = {"configurable": {"thread_id": st.session_state.user_id}}
    messages = [HumanMessage(content=input_text)]
    output_text = graph.invoke({'messages': messages}, config=thread)
    return output_text['messages'][-1].content


# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input handling
if user_input := st.chat_input("Share your thoughts..."):
    # Display and store the user's message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    bot_response = chatbot_response(user_input)
    # Display and store the bot's response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
