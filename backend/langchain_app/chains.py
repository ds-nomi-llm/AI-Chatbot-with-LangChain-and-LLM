from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
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