
# AI Chatbot with LangChain and LLM

This is an AI chatbot built using LangChain and OpenAI's LLMs. It can answer questions based on custom documents like PDFs and text files. It’s my first AI project, created after learning from CampusX tutorials.


## Tech Stack

**Client:** - 
- Streamlit

**Server:** 
- Python
- FastAPI
- LangChain
- OpenAI API (GPT-3.5/4)
- FAISS (Vector Store)


## Features

- Answer user queries based on ingested documents
- Streamlit-based interactive UI
- FastAPI backend for LLM processing
- Uses LangChain for chaining logic
- Uses LangChain-openai fro llm (gpt-3.5-turbo)
- History of chat printing like chatgpt


## Installation

Install my-project with npm

```bash
  git clone https://github.com/ds-nomi-llm/AI-Chatbot-with-LangChain-and-LLM.git
  cd AI-Chatbot-with-LangChain-and-LLM
  npm install
```
    

## Install Dependencies
pip install -r requirements.txt


## Start Backend
uvicorn backend.main:app --reload


## Start Frontend
streamlit run frontend/app.py


## Acknowledgements
- Thanks to [CampusX](https://www.youtube.com/@campusx-official) for the guidance.
- Inspired by the official LangChain documentation.