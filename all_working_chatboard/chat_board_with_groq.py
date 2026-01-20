import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

# ---------- Page setup ----------
st.set_page_config(page_title="Yogesh Patel")
st.title("Welcome To The Chatboard 🚀")

# ---------- Init Groq client ----------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Display history ----------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------- Chat input ----------
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Placeholder for streaming text
    response_box = st.chat_message("assistant")
    stream_placeholder = response_box.empty()

    full_response = ""

    # ---------- Streaming completion ----------
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages,
        temperature=1,
        max_completion_tokens=1024,
        stream=True,
    )

    for chunk in completion:
        token = chunk.choices[0].delta.content
        if token:
            full_response += token
            stream_placeholder.write(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
