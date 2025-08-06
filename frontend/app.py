import streamlit as st
import requests
import json

st.set_page_config(page_title='Langchain AI Chatbot', layout='centered')

st.title("LangChain-Powered AI Chatbot")
st.markdown("Ask anything based on your ingested documents!")

BASE_URL = 'http://localhost:8000'

if st.sidebar.button('Ingest Document'):
    with st.spinner('Reading and embedding documents...'):
        response = requests.get(f"{BASE_URL}/ingest").json()
        st.success(response['status'])

user_input = st.text_input('Your Question:')

if user_input:
    with st.spinner("Thinking..."):
        payload = {'question':user_input}
        res = requests.post(
            f"{BASE_URL}/chat",
            json = payload
        )
        if res.status_code == 200:
            st.write("🤖", res.json()['answer'])
        else:
            st.error(f"Error {res.status_code}: {res.text}")

