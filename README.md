# Chef Ali

Chef Ali is a simple Streamlit cooking assistant powered by the Groq API. It answers food and cooking questions and keeps the conversation history during the current Streamlit session.

## Features

- Conversational chat interface built with Streamlit
- Groq-powered responses using `openai/gpt-oss-120b`
- Conversation history stored in `st.session_state`
- Responses limited to food and cooking topics

## Requirements

- Python 3.10 or newer
- A Groq API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TahaHusnainNizami/steamlit_chatbot.git
   cd steamlit_chatbot
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install streamlit groq python-dotenv
   ```

4. Create a local `.env` file based on `.env.example` and add your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Never commit `.env` or expose your API key publicly.

## Run the app

Start the Streamlit application with:

```powershell
streamlit run app.py
```

Streamlit will display a local URL, usually `http://localhost:8501`.

## Project structure

```text
.
├── app.py
├── .env.example
├── .gitignore
└── README.md
```

## Security

API keys are loaded from the local `.env` file and are excluded from Git using `.gitignore`. If an API key is ever committed or shared, revoke it immediately and create a replacement key.
