import requests
import streamlit as st

st.set_page_config(page_title='Yogesh Patel ChatBoard')
st.title('Chatboard Created By yogesh Patel Using Python')

if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    role,text=msg
    if role=='user':
        st.chat_message("user").write(text)
    else:
        st.chat_message("assistant").write(text)
if prompt := st.chat_input("Type Your Message..."):

    st.session_state.messages.append(("user",prompt))
    st.chat_message("user").write(prompt)

    with st.spinner("Thinking..."):
        response=requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"llama3","prompt":prompt,"stream":False},

        )
    if response.status_code==200:
        content=response.json().get("response","")
    else:
        content=f"Error :{response.text}"
    st.session_state.messages.append(('assistant',content))
    st.chat_message('assistant').write(content)


# import streamlit as st
# import requests

# # --- Streamlit UI setup ---
# st.set_page_config(page_title="Local LLM Chatbot", page_icon="🧠")
# st.title("🧠 Local Chatbot using Ollama (LLaMA3)")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for msg in st.session_state.messages:
#     role, text = msg
#     if role == "user":
#         st.chat_message("user").write(text)
#     else:
#         st.chat_message("assistant").write(text)

# # User input
# if prompt := st.chat_input("Type your message..."):
#     # Add user message
#     st.session_state.messages.append(("user", prompt))
#     st.chat_message("user").write(prompt)

#     # Send to Ollama local server
#     with st.spinner("Thinking..."):
#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={"model": "llama3", "prompt": prompt, "stream": False},
#         )

#     if response.status_code == 200:
#         content = response.json().get("response", "")
#     else:
#         content = f"Error: {response.text}"

#     # Add model response
#     st.session_state.messages.append(("assistant", content))
#     st.chat_message("assistant").write(content)
