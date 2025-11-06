# import requests
# import streamlit as st

# st.set_page_config(page_title="Yogesh Patel Dashboard")
# st.title("Chatboard Created By Yogesh Patel Using Python")

# if "messages" not in st.session_state:
#     st.session_state.messages=[]
# for msg in st.session_state.messages:
#     role,text=msg

#     if role=='user':
#         st.chat_message('user').write(text)
#     else:
#         st.chat_message('assistant').write(text)
# if prompt:=st.chat_input("Type Your Message..."):
#     st.session_state.messages.append(('user',prompt))
#     st.chat_message('user').write(prompt)

#     with st.spinner("Thinking..."):
#         response=requests.post(
#             'http://localhost:11434/api/generate',
#             json={'model':"llama3",'prompt':prompt,'stream':False},
#         )
#     if response.status_code==200:
#         content=response.json().get('response',"")
#     else:
#         content=f"Error {response.text}"
#     st.session_state.messages.append(('assistant',content))
#     st.chat_message('assistant').write(content)


# import streamlit as st
# import requests

# st.set_page_config(page_title='Yogesh DashBoard')
# st.title("Yogesh Patel ChatBoard")

# if "messages" not in st.session_state:
#     st.session_state.messages=[]
# for msg in st.session_state.messages:
#     role,text=msg
#     if role=='user':
#         st.chat_message('user').write(text)
#     else:
#         st.chat_message('assistant').write(text)

# if prompt:=st.chat_input("Type Your message"):
#     st.session_state.messages.append(('user',prompt))
#     st.chat_message('user').write(prompt)

#     with st.spinner("Thinking..."):
#         response=requests.post(
#             "http://localhost:11434/api/generate",
#             json={'model':'llama3','prompt':prompt,'stream':False},

#         )
#     if response.status_code==200:
#         content=response.json().get('response','')
#     else:
#         content=f"Error {response.text}"
    
#     st.session_state.messages.append(('assistant',content))
#     st.chat_message('assistant').write(content)


import streamlit as st
import requests

st.set_page_config(page_title="Yogesh Patel")
st.title("Yogesh Patel ChatBoard")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    role,text=msg

    if role=='user':
        st.chat_message('user').write(text)
    else:
        st.chat_message('assistant').write(text)

if prompt:= st.chat_input("Type Your Messages..."):
    st.session_state.messages.append(('user',prompt))
    st.chat_message('user').write(prompt)

    with st.spinner("Thinking..."):
        response=requests.post(
            'http://localhost:11434/api/generate',
            json={'model':'llama3','prompt':prompt,'stream':False},

        )
    if response.status_code==200:
        content=response.json().get('response','')
    else:
        content=f"Error: {response.text}"
    
    st.session_state.messages.append(('assistant',content))
    st.chat_message('assistant').write(content)