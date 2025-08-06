from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def get_embedding_model():
    return OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
