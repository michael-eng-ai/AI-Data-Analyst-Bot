# 🤖 AI Data Analyst Bot

**Project 5 from the Cloud Strategy Portfolio.**

An intelligent agent that acts as a Data Analyst, utilizing Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to query Data Warehouses and company documentation using natural language.

---

## 🏗️ Architecture

This project implements a hybrid **Text-to-SQL + RAG** pipeline:
1. **Semantic Routing:** Learns the intent of the user's question.
2. **Text-to-SQL:** If it's a quantitative question, it generates a strict SQL Query and executes it against Google BigQuery.
3. **Advanced RAG:** If it's a qualitative question, it searches the Vector Database (Pinecone) containing business glossaries and metrics documentation.
4. **Token Optimization:** Uses local embeddings and summary truncation to save costly LLM tokens.

## 🚀 Tech Stack

*   **Cloud:** Google Cloud Platform (BigQuery)
*   **Infrastructure as Code:** Terraform
*   **CI/CD:** GitHub Actions
*   **AI/LLM:** Google Gemini API / Groq
*   **Orchestration:** LangChain / LangGraph
*   **Frontend:** Streamlit

## 💻 Local Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```
