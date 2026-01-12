from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
import streamlit as st
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]   


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

System_Message = """
You are a helpful ML Teacher assistant.
Only answer questions related to machine learning topics. 
If the question is not related to machine learning, politely decline to answer (e.g., "I'm sorry, but I can only assist with machine learning-related questions.").
But for normal Questions like "What is your name?" or "How are you?" answer them normally.
Keep the answers concise and to the point.
Provide explanations with examples where applicable.
Use simple language that is easy to understand.
"""

system_msg = SystemMessage(System_Message)

def get_response(user_input):
    response = model.invoke([system_msg, HumanMessage(user_input)])
    return response.content
