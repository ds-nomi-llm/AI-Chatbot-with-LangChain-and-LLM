import streamlit as st
import requests
import json

st.set_page_config(page_title='Langchain AI Chatbot', layout='centered')

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

st.title("LangChain-Powered AI Chatbot")
st.markdown("Ask anything based on your ingested documents!")

BASE_URL = 'http://localhost:8000'

if st.sidebar.button('Ingest Document'):
    with st.spinner('Reading and embedding documents...'):
        response = requests.get(f"{BASE_URL}/ingest").json()
        st.success(response['status'])

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    #printig user message
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    #printing ai message
    payload = {'question':user_input}
    res = requests.post(

        f"{BASE_URL}/chat",
        json = payload
    )
    if res.status_code == 200:
        st.session_state['message_history'].append({'role':'assistant','content':res.json()['answer']})
        with st.chat_message('assistant'):
            st.text(res.json()['answer'])
    else:
        st.error(f"Error {res.status_code}: {res.text}")