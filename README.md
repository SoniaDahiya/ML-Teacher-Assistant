# 💬 ML Teacher Assistant

A simple chatbot application that helps answer machine learning questions using Google's Gemini AI.

## 📝 About

This is a learning project that demonstrates how to build an AI-powered chatbot using Streamlit and LangChain. The assistant is designed to help students learn about machine learning concepts by answering their questions in a clear and concise manner.

**Developer:** Sonia

## ✨ Features

- 💬 Interactive chat interface
- 🤖 Powered by Google's Gemini 2.5 Flash model
- 📚 Focused on machine learning topics
- 🎨 User-friendly interface built with Streamlit
- 💾 Maintains chat history during the session

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **LangChain** - Framework for building LLM applications
- **Google Generative AI (Gemini)** - Language model for responses

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI

## 🚀 Installation

1. Clone or download this project

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Update the `GOOGLE_API_KEY` in `main.py` with your own API key

## ▶️ How to Run

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 💡 How to Use

1. Open the application in your browser
2. Type your machine learning question in the chat input
3. Press Enter or click Send
4. The assistant will respond with helpful information
5. Continue asking questions - the chat history is preserved!

## 📖 What It Does

The ML Teacher Assistant:
- Answers questions related to machine learning topics
- Politely declines non-ML questions (except basic conversational queries)
- Provides concise, easy-to-understand explanations
- Uses examples to help clarify concepts

## 🎓 Learning Project

This project is created for learning purposes to understand:
- Building chatbot interfaces with Streamlit
- Integrating LangChain with large language models
- Working with Google's Gemini API
- Managing conversation state and chat history
- Creating system prompts for specific use cases

## ⚠️ Note

Remember to keep your API keys secure and never commit them to public repositories!

## 📄 License

This is a learning project and is free to use and modify.
