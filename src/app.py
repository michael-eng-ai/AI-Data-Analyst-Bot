import os
import streamlit as st
from dotenv import load_dotenv

# Import our custom agent functions
# from src.agent.sql_agent import create_sql_agent
# from src.agent.rag_agent import create_rag_chain

load_dotenv()

st.set_page_config(page_title="AI Data Analyst Bot", page_icon="🤖", layout="wide")

st.title("🤖 AI Data Analyst Bot (Text-to-SQL + RAG)")
st.markdown("""
Este agente inteligente conecta-se ao BigQuery e processa documentações usando RAG.
Faça uma pergunta sobre seus dados em linguagem natural!
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ex: Qual foi o total de vendas na região Sudeste em 2023?"):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent Response placeholder
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # TODO: Implement Semantic Router here
        # Example logic:
        # if is_sql_question(prompt):
        #     response = sql_agent.run(prompt)
        # else:
        #     response = rag_chain.run(prompt)
        
        # Fake response for initial setup
        response = f"Simulação de Resposta: O modelo identificou sua pergunta ('{prompt}') e em breve vai gerar a Query SQL para responder."
        
        message_placeholder.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
