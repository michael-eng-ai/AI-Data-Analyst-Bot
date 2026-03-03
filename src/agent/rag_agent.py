"""
AI Data Analyst Bot - RAG Agent logic
"""

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def create_rag_chain(llm, persist_dir="data/chroma_db"):
    # Load Vector DB
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # System instruction for RAG
    system_prompt = (
        "Você é um Analista de Dados respondendo a dúvidas de negócios com base em documentação técnica.\n"
        "Use APENAS os contextos fornecidos abaixo para responder à pergunta.\n"
        "Se a resposta não estiver no contexto, diga que não encontrou informações na base de conhecimento.\n"
        "Sempre responda em PT-BR (Português do Brasil).\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain
