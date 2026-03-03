"""
Script to create dummy markdown documentation for RAG testing.
"""

import os

def create_dummy_docs(docs_dir="data/docs"):
    os.makedirs(docs_dir, exist_ok=True)
    
    # Doc 1: Business Metrics
    with open(f"{docs_dir}/metricas_negocio.md", "w") as f:
        f.write("""# Glossário de Métricas de Negócio

## Faturamento Total
O Faturamento Total é calculado pela soma da multiplicação entre o preço do produto (`price`) e a quantidade vendida (`quantity`) na tabela de vendas. Não consideramos devoluções nesta versão simplificada.

## Cliente VIP
Um cliente é considerado VIP se a soma total de suas compras no ano ultrapassar R$ 5.000,00.

## Regras de Desconto B2B
Clientes do segmento 'B2B' têm direito a 10% de desconto em compras com quantidade superior a 50 unidades do mesmo produto.
""")

    # Doc 2: Company Info
    with open(f"{docs_dir}/sobre_empresa.md", "w") as f:
        f.write("""# Sobre a Empresa DataCo

A DataCo foi fundada em 2020 com a missão de simplificar o e-commerce no Brasil. 
Nossos galpões logísticos principais estão localizados em São Paulo (SP) e Minas Gerais (MG), o que garante prazos de entrega menores para a região Sudeste.
A equipe de Engenharia de Dados é responsável por garantir a governança através do BigQuery e integração com IA.
""")

    print(f"Documentos gerados com sucesso em {docs_dir}/")

if __name__ == "__main__":
    create_dummy_docs()
