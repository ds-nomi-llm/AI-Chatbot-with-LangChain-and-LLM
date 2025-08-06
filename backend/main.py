from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from langchain_app.loaders import load_and_split_docs
from langchain_app.vectorstore import create_vector_store, load_vector_store
from langchain_app.chains import build_qa_chain
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Allow frontend access (e.g., Streamlit/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "LangChain Chatbot Backend is Running!"}

@app.get("/ingest")
def ingest_docs():
    chunks = load_and_split_docs("../data/documents")
    create_vector_store(chunks)
    return {"status": "Data ingested and vector store created."}

class Query(BaseModel):
    question : Annotated[str, Field(..., description='Query to ask from chatbot based on your pdfs')]

@app.post("/chat")
def ask_question(query: Query):
    vectorstore = load_vector_store()
    qa_chain = build_qa_chain(vectorstore)
    response = qa_chain.invoke({'input':query.question})
    return {"answer": response['answer']}
