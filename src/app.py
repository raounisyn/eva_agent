import streamlit as st
from chatbot import Chatbot
import time

# Set page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for chat history
if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a title and description
st.title("🤖 EVA AI")
st.markdown("""
This chatbot uses the Nemotron model to provide intelligent responses. 
You can ask it questions or have a conversation about various topics.
""")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get chatbot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate typing effect
        response = st.session_state.chatbot.process_message(prompt)
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add a sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
    This chatbot is powered by:
    - Nemotron LLM
    - LangChain
    - Streamlit
    
    The chatbot maintains conversation history and provides intelligent responses
    to your queries.
    """)
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chatbot = Chatbot()
        st.rerun() 