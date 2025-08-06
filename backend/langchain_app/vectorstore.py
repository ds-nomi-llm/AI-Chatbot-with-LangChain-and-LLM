from langchain_community.vectorstores import FAISS
from langchain_app.embeddings import get_embedding_model
import os

def create_vector_store(chunks, persist_path="vector_store"):
    embedding_model = get_embedding_model()
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(persist_path)

def load_vector_store(persist_path="vector_store"):
    embedding_model = get_embedding_model()
    return FAISS.load_local(persist_path, embedding_model, allow_dangerous_deserialization=True)
