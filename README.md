# Wellbeing Companion Chatbot 🤖

This project is a self-care chatbot assistant built to provide empathetic, supportive guidance for users dealing with personal and emotional challenges. By leveraging LangGraph, Tavily, SQLite, and Streamlit, the chatbot delivers an interactive and context-aware experience that can address various user concerns thoughtfully.


https://github.com/user-attachments/assets/32b47354-8d23-4dcd-9672-3ca2ea78146f


## Overview

The chatbot is designed to engage users in a warm, supportive conversation, with a focus on providing contextually accurate responses. It uses LangGraph to build sophisticated workflows and Tavily for online health-related searches, ensuring both empathetic responses and access to reliable information when needed. Conversations are managed using SQLite for long-term memory, and the user interface is built with Streamlit.
Why LangGraph?

LangGraph enabled us to design a highly detailed workflow, allowing the assistant to perform effectively in conversations of varying complexity. Specifically:

  - Graph-based Workflow: LangGraph facilitated the creation of an adaptive, multi-step workflow that could dynamically branch based on user input and needs.
  - Memory Management: By integrating LangGraph with SQLite, we implemented persistent memory storage, allowing the assistant to remember conversation history and respond in a way that feels personal and consistent over time.
  - Flexibility with External Sources: LangGraph was instrumental in coordinating Tavily's health search capability to fetch trusted solutions when the conversation required medical insights for extreme health conditions.
  - Streamlit Interface: An interactive UI is built with Streamlit, allowing users to chat comfortably with the bot in a friendly, engaging interface.

  
![Wellbeing-Companion-Graph](https://github.com/user-attachments/assets/daf833b4-90d3-4817-8316-805dc848619d)


The image above represents a workflow built using Langgraph. The workflow begins with a listener_agent, which collects and interprets user inputs to identify key concerns. The process can then move to the health_advisor_agent, which assesses any health-related queries or provides expert guidance if needed. Next, the assistant_agent synthesizes this information to generate empathetic, personalized responses. Finally, the summarization_agent consolidates the conversation history, creating a brief summary that enhances continuity for future interactions.

This structured approach enables seamless, contextual assistance by guiding the chatbot through a logical series of agents. Each agent in the workflow has a clear, defined role, contributing to an effective and responsive user experience.

## Deployment

The project has been deployed on both Huggingface Spaces and Streamlit Cloud to make it easily accessible to users:

  - Huggingface Spaces: [HuggingFace Spaces Wellbeing Companion](https://huggingface.co/spaces/chescore/Wellbeing-Companion-with-Langgraph)
  - Streamlit Cloud: [Deployed Streamlit Wellbeing Companion](https://wellbeing-companion.streamlit.app/)

## Key Features

  - Empathetic, Guided Responses: The assistant provides personalized responses that respect and validate the user's feelings, offering advice only when appropriate.
  - Context-aware Memory: The bot leverages SQLite for persistent memory, keeping track of previous interactions for a consistent, supportive conversation flow.
  - Reliable Health Sources: Using Tavily, the assistant can fetch professional advice on health issues, enriching its responses when medical context is essential.
  - Scalable Interface: Streamlit's user-friendly interface supports a smooth user experience across both desktop and mobile platforms.

## Installation and Setup

1) Clone this repository:

        git clone https://github.com/Stephen-Echessa/Wellbeing-Companion-with-Langgraph.git
        cd Wellbeing-Companion-with-Langgraph

2) Install the necessary dependencies:

        pip install -r requirements.txt

3) Set up your environment variables for API keys.

4) Run the application locally:

        streamlit run app.py

## Usage

Once launched, the chatbot will guide users through a supportive conversation, drawing on previous messages for context and providing researched insights on request.

## Future Improvements
  - Add Audio Capabilities
  - Gain more data from health professionals
