# 💬 ML Teacher Assistant

A simple chatbot application that helps answer machine learning questions using Google's Gemini AI.

## 🌐 Live Demo

**[Try it now!](https://sonia-ml-teacher-assistant.streamlit.app/)**

The application is deployed and ready to use at: https://sonia-ml-teacher-assistant.streamlit.app/

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
- **Google Generative AI (Gemini)** - Language model (Gemini 2.5 Flash model)

## 🏗️ Project Structure

```
ML-Teacher-Assistant-/
├── app.py              # Main Streamlit application interface
├── main.py             # Core logic and AI model integration
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── LICENSE            # License file
```

### File Descriptions

- **`app.py`**: Contains the Streamlit UI code, manages chat history, handles user input/output, and displays the chat interface.
- **`main.py`**: Implements the AI logic using LangChain and Google Gemini API, defines the system prompt, and provides the response generation function.
- **`requirements.txt`**: Lists all Python dependencies required for the project.

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI

## 🚀 Installation

### Option 1: Quick Start (Local)

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd ML-Teacher-Assistant-
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   
   You have two options:
   
   **Option A: Environment Variable (Recommended for security)**
   ```bash
   # On Windows PowerShell
   $env:GOOGLE_API_KEY="your-api-key-here"
   
   # On Windows Command Prompt
   set GOOGLE_API_KEY=your-api-key-here
   
   # On macOS/Linux
   export GOOGLE_API_KEY=your-api-key-here
   ```
   
   Then update `main.py` to read from environment variable:
   ```python
   os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
   ```
   
   **Option B: Direct Configuration (Not recommended for production)**
   
   Update the `GOOGLE_API_KEY` in `main.py` with your own API key.

### Option 2: Using Streamlit Cloud (Deployment)

1. Fork this repository to your GitHub account
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect your forked repository
4. Add your `GOOGLE_API_KEY` in the Streamlit Cloud secrets management
5. Deploy!

## 🔑 Getting a Google API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key
5. Use it in your project as described in the Installation section

**Important:** Keep your API key secure and never commit it to public repositories!

## ▶️ How to Run

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 💡 How to Use

1. **Access the application:**
   - **Online:** Visit https://sonia-ml-teacher-assistant.streamlit.app/
   - **Locally:** Run `streamlit run app.py` and open http://localhost:8501

2. **Start chatting:**
   - Type your machine learning question in the chat input box at the bottom
   - Press Enter or click the send button

3. **Get answers:**
   - The assistant will process your question and respond
   - Responses are focused on machine learning topics

4. **Continue the conversation:**
   - Ask follow-up questions
   - The chat history is preserved throughout your session
   - Refresh the page to start a new conversation

### Example Questions You Can Ask:

- "What is the difference between supervised and unsupervised learning?"
- "Explain gradient descent in simple terms"
- "What is overfitting and how can I prevent it?"
- "How does a neural network work?"
- "What is the purpose of cross-validation?"

## 📖 What It Does

The ML Teacher Assistant:
- ✅ Answers questions related to machine learning topics
- ✅ Provides concise, easy-to-understand explanations
- ✅ Uses examples to help clarify concepts
- ✅ Handles basic conversational queries (greetings, etc.)
- ❌ Politely declines non-ML questions with a helpful message

### System Behavior

The assistant is configured with a specialized system prompt that:
- Focuses exclusively on machine learning education
- Maintains a friendly and approachable tone
- Provides clear, student-friendly explanations
- Uses examples to illustrate concepts
- Keeps answers concise and to the point

## 🎓 Learning Project

This project is created for learning purposes to understand:
- 🖥️ Building interactive chatbot interfaces with Streamlit
- 🔗 Integrating LangChain with large language models
- 🤖 Working with Google's Gemini API
- 💬 Managing conversation state and chat history
- 📝 Creating effective system prompts for specific use cases
- ☁️ Deploying AI applications to the cloud

## 🔧 Customization

You can customize the assistant by modifying `main.py`:

1. **Change the AI Model:**
   ```python
   model = ChatGoogleGenerativeAI(model="gemini-pro")
   ```

2. **Modify the System Prompt:**
   Edit the `System_Message` variable to change the assistant's behavior, tone, or focus area.

3. **Adjust Response Style:**
   Update the prompt instructions to make responses more detailed, technical, or beginner-friendly.

## 🐛 Troubleshooting

### Common Issues:

**Issue: "Invalid API Key" error**
- Solution: Verify your Google API key is correct and active
- Check that the API key has Gemini API access enabled

**Issue: Application won't start**
- Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using Python 3.8 or higher: `python --version`

**Issue: Slow responses**
- Solution: This may be due to API rate limits or network latency
- Consider upgrading your API plan if using heavily

**Issue: Chat history not persisting**
- Solution: This is expected behavior - chat history resets on page refresh
- To persist history, you would need to implement database storage

## 🤝 Contributing

This is a learning project, but contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share improvements

## 📞 Contact

**Developer:** Sonia

For questions or feedback about this project, feel free to open an issue in the repository.

## ⚠️ Note

Remember to keep your API keys secure and never commit them to public repositories!

## 📄 License

This is a learning project and is free to use and modify.

---

## 🌟 Quick Links

- **Live Application:** https://sonia-ml-teacher-assistant.streamlit.app/
- **Streamlit Documentation:** https://docs.streamlit.io/
- **LangChain Documentation:** https://python.langchain.com/
- **Google Gemini AI:** https://ai.google.dev/

---

**Made with ❤️ by Sonia**
