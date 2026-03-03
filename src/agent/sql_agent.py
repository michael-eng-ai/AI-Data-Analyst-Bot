"""
AI Data Analyst Bot - Text-to-SQL logic
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent as langchain_create_sql_agent
from langchain.agents.agent_types import AgentType

def init_db_connection(db_uri: str) -> SQLDatabase:
    """Initializes the SQLAlchemy connection via Langchain SQLDatabase."""
    return SQLDatabase.from_uri(db_uri)

def create_sql_agent(db: SQLDatabase, llm: ChatGoogleGenerativeAI):
    """Creates the LangChain SQL Agent using Google Gemini."""
    
    # Custom instructions for the agent to behave like a senior analyst
    prefix = '''
    Você é um Engenheiro e Analista de Dados Sênior. 
    Sua função é interagir com um banco de dados SQL para responder a perguntas de negócios.
    Siga estas regras estritamente:
    1. Sempre verifique o schema das tabelas antes de criar uma query.
    2. Crie queries eficientes e precisas.
    3. Quando o usuário perguntar algo genérico, faça agrupamentos úteis (ex: GROUP BY).
    4. Responda APENAS em PT-BR (Português do Brasil).
    5. Juntamente com a resposta analítica, mostre a Query SQL gerada em um bloco de código markdown.
    '''
    
    agent_executor = langchain_create_sql_agent(
        llm=llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5,
        prefix=prefix
    )
    
    return agent_executor
