# AI Data Analyst Bot

**Project 5 from the Cloud Strategy Portfolio.**

An intelligent agent that acts as a Data Analyst, utilizing Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to query Data Warehouses and company documentation using natural language processing interfaces.

---

## Architecture

This project implements a hybrid Text-to-SQL + RAG pipeline designed for structural accuracy and hallucination prevention:
1. **Semantic Routing:** Analyzes user intent to determine required analytical actions.
2. **Text-to-SQL Conversion:** Processes quantitative prompts to generate strict SQL Queries, executing them autonomously against Google BigQuery instances.
3. **Advanced Retrieval-Augmented Generation (RAG):** Manages qualitative requests by searching the target Vector Database (Pinecone). It correlates established business glossaries and metrics definition documentation.
4. **Token Optimization Strategies:** Employs local embeddings and summary truncation mechanisms to constrain the computational token overhead required for external LLM evaluation loops.

## Technical Stack Overview

*   **Cloud Infrastructure:** Google Cloud Platform (BigQuery)
*   **Infrastructure as Code:** Terraform
*   **Continuous Integration/Delivery:** GitHub Actions
*   **AI Models and Integration:** Google Gemini API / Groq
*   **Agentic Orchestration Systems:** LangChain / LangGraph
*   **Frontend Data Interface:** Streamlit

## Local Execution and Environment Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```
