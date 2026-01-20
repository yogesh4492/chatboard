import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ---------- Load env ----------
load_dotenv()

# ---------- Configure Gemini ----------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",  # ✅ FIXED MODEL
    generation_config={
        "temperature": 1,
        "top_p": 1,
        "max_output_tokens": 2048,
    },
)

# ---------- Page setup ----------
st.set_page_config(page_title="Yogesh Patel")
st.title("Welcome To The Chatboard 🚀")

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

    # Convert history for Gemini
    gemini_history = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        gemini_history.append(
            {"role": role, "parts": [msg["content"]]}
        )

    response_box = st.chat_message("assistant")
    placeholder = response_box.empty()
    full_response = ""

    # ---------- Streaming ----------
    response = model.generate_content(
        gemini_history,
        stream=True
    )

    for chunk in response:
        if chunk.text:
            full_response += chunk.text
            placeholder.write(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
