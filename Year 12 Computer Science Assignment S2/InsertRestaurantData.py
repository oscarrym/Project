import sqlite3

def setup_database():
    # Connect to the SQLite database
    conn = sqlite3.connect(r'Food Delivery Service Assignment Sheet Updated.csv')
    cursor = conn.cursor()

    # Create tables with the correct structure
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
                   OrderID INTEGER PRIMARY KEY,
                   OrderDate INTEGER NOT NULL,
                   Quantity INTEGER NOT NULL,
                   TotalAmount INTEGER NOT NULL
                   )               
                   ''')