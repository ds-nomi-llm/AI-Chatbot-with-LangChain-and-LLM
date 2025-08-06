from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


from langchain_community.vectorstores import FAISS
from langchain_app.embeddings import get_embedding_model
import os


def load_and_split_docs(directory: str):
    all_docs = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
        elif filename.endswith(".txt"):
            loader = TextLoader(filepath)
        else:
            continue

        documents = loader.load()
        all_docs.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(all_docs)

# data = load_and_split_docs('../data/documents')

# print(data[3])

def create_vector_store(chunks, persist_path="vector_store"):
    embedding_model = get_embedding_model()
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(persist_path)

# create_vector_store(data, persist_path='vector_store')

def load_vector_store(persist_path="vector_store"):
    embedding_model = get_embedding_model()
    return FAISS.load_local(persist_path, embedding_model, allow_dangerous_deserialization=True)

vector_store = load_vector_store()
# retiever = vector_store.as_retriever()

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

def build_qa_chain(vectorstore):
    prompt = PromptTemplate(
        template = """
        Answer any use questions based solely on the context below:

        <context>
        {context}
        </context>
        <question>
        {input}
        </question>
"""
    )    
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0.2, model ='gpt-3.5-turbo')  # or gpt-3.5-turbo
    combine_docs_chain = create_stuff_documents_chain(llm,
                                            prompt)
    qa_chain = create_retrieval_chain(
        retriever,
        combine_docs_chain
    )
    return qa_chain

query = 'What is Langchain used for?'

chain = build_qa_chain(vector_store)
result = chain.invoke({'input':query})

print(type(result))