import os
import streamlit as st
from dotenv import load_dotenv

# Import our custom agent functions
from agent.sql_agent import init_db_connection, create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(page_title="AI Data Analyst Bot", page_icon="🤖", layout="wide")

st.title("🤖 AI Data Analyst Bot (Text-to-SQL + RAG)")
st.markdown("""
Este agente inteligente conecta-se ao banco de dados e processa documentações usando RAG.
Faça uma pergunta sobre seus dados em linguagem natural!

**Exemplos de Teste (SQLite):**
- *Qual foi o faturamento total por categoria de produto?*
- *Quantos clientes nós temos no estado de SP?*
- *Qual o cliente que mais comprou em valor total?*
""")

# Setup Gemini API Key logic (require user to input it or load from env)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.sidebar.warning("⚠️ Chave da API do Google Gemini não encontrada.")
    api_key_input = st.sidebar.text_input("Insira sua GOOGLE_API_KEY:", type="password")
    if api_key_input:
        os.environ["GOOGLE_API_KEY"] = api_key_input
        api_key = api_key_input
        st.rerun()
    else:
        st.stop()

# Initialize resources (Cache to avoid reconnecting on every render)
@st.cache_resource
def setup_agent():
    # Model definition
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", # or gemini-2.0-flash depending on your tier
        temperature=0,
        google_api_key=api_key
    )
    
    # DB connection (Local SQLite for V1)
    db_uri = f"sqlite:///data/ecommerce_dummy.db"
    db = init_db_connection(db_uri)
    
    # Create Agent
    return create_sql_agent(db, llm)

try:
    sql_agent = setup_agent()
except Exception as e:
    st.error(f"Erro ao inicializar o agente: {e}")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Pergunte algo ao seu Banco de Dados..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent Response placeholder
    with st.chat_message("assistant"):
        with st.spinner("Analisando o banco de dados e gerando a query SQL..."):
            try:
                # TODO: Implement Semantic Router here later for RAG vs SQL
                # Currently hardcoded to SQL Agent
                response = sql_agent.invoke({"input": prompt})
                output_text = response.get("output", "Desculpe, não consegui gerar uma resposta.")
                st.markdown(output_text)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": output_text})
            
            except Exception as e:
                error_msg = f"Erro na execução da Query: {e}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
