"""
Script to generate a local SQLite database with dummy e-commerce data.
This will be used for testing the Text-to-SQL Agent before pointing it to BigQuery.
"""

import sqlite3
import random
from datetime import datetime, timedelta

def create_dummy_database(db_path="data/ecommerce_dummy.db"):
    # Connect or create the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Customers Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        state TEXT NOT NULL,
        segment TEXT NOT NULL
    )
    ''')

    # Create Products Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')

    # Create Sales Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        sale_date DATE NOT NULL,
        quantity INTEGER NOT NULL,
        total_amount REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    # Insert Dummy Customers
    states = ["SP", "RJ", "MG", "PR", "RS", "BA", "PE", "CE"]
    segments = ["B2B", "B2C"]
    
    customers_data = []
    for i in range(1, 51):
        customers_data.append((i, f"Cliente {i}", random.choice(states), random.choice(segments)))
    
    cursor.executemany('INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)', customers_data)

    # Insert Dummy Products
    categories = ["Eletrônicos", "Móveis", "Livros", "Escritório"]
    
    products_data = []
    for i in range(1, 21):
        price = round(random.uniform(50.0, 3000.0), 2)
        products_data.append((i, f"Produto {i}", random.choice(categories), price))
        
    cursor.executemany('INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)', products_data)

    # Insert Dummy Sales
    sales_data = []
    start_date = datetime(2023, 1, 1)
    
    for _ in range(500):
        customer_id = random.randint(1, 50)
        product_id = random.randint(1, 20)
        
        # Calculate random date in 2023
        random_days = random.randint(0, 364)
        sale_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        quantity = random.randint(1, 10)
        
        # Get product price for total amount
        cursor.execute('SELECT price FROM products WHERE product_id = ?', (product_id,))
        price = cursor.fetchone()[0]
        total_amount = round(price * quantity, 2)
        
        sales_data.append((customer_id, product_id, sale_date, quantity, total_amount))

    cursor.executemany('INSERT INTO sales (customer_id, product_id, sale_date, quantity, total_amount) VALUES (?, ?, ?, ?, ?)', sales_data)

    conn.commit()
    conn.close()
    print(f"Banco de dados criado com sucesso em: {db_path}")
    print("- 50 Clientes gerados")
    print("- 20 Produtos gerados")
    print("- 500 Vendas geradas")

if __name__ == "__main__":
    create_dummy_database()
