import streamlit as st
from main import get_response

st.set_page_config(page_title="ML Teacher Assistant", page_icon="💬")

st.title("💬 ML Teacher Assistant")
st.markdown("Welcome to ML Teacher Assistant! Ask me anything.")
st.markdown("Developed by: Sonia")
st.markdown("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Loading indicator
    with st.spinner("Thinking..."):
        bot_response = get_response(user_input)
    

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    # Display bot message
    with st.chat_message("assistant"):
        st.markdown(bot_response)
