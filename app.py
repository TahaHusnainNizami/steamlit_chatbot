from groq import Groq 
import streamlit as st
from dotenv import load_dotenv
import os 
load_dotenv()

Client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"

SYSTEM = (
    "You are Chef Ali, a friendly cooking assistant. "
    "Only talk about food and cooking. Keep answers under three sentences."
)

st.title('chef Ali')
st.caption('Ask me anything about cooking!')

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM}]

for m in st.session_state.messages:
    if m["role"] != "system":
        with st.chat_message(m["role"]):
            st.write(m["content"])


user_text = st.chat_input('type your message...')
if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    response = Client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages,
        max_tokens=300,
    )
    reply = response.choices[0].message

    st.session_state.messages.append({"role": "assistant", "content": reply.content})
    with st.chat_message("assistant"):
        st.write(reply.content)
   