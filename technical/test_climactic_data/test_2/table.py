#test local, validation queries
import sqlite3
import pandas as pd

def local():
    conn = sqlite3.connect(":memory:")

    #tables and data
    conn.executescript("""
        CREATE TABLE clients (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            city TEXT, 
            active BOOLEAN
        );
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY, 
            client_id INTEGER, 
            value REAL, 
            status TEXT
        );

        INSERT INTO clients VALUES 
        (1, 'test1', 'porto alegre', 1),
        (2, 'test2', 'floripa', 1),
        (3, 'test3', 'garopaba', 0),
        (4, 'test4', 'sao paulo', 1);

        INSERT INTO orders VALUES 
        (101, 1, 1000, 'paid'),
        (102, 1, 2000, 'pending'),
        (103, 2, 3000, 'paid'),
        (104, 3, 4000, 'paid');
    """)

    #query a
    query_a = """
        SELECT DISTINCT c.name 
        FROM clients c
        INNER JOIN orders p ON c.id = p.client_id
        WHERE c.active = 1 AND p.status = 'paid';
    """
    print("[A] Clients paids:")
    print(pd.read_sql_query(query_a, conn))
    print("\n")

    #query b
    query_b = """
        SELECT c.city, SUM(p.value) AS total_spent
        FROM clients c
        INNER JOIN orders p ON c.id = p.client_id
        WHERE p.status = 'pago'
        GROUP BY c.city
        ORDER BY total_spent DESC;
    """
    print("Total value by city:")
    print(pd.read_sql_query(query_b, conn))
    print("\n")

    #query c
    query_c = """
        SELECT c.name 
        FROM clients c
        LEFT JOIN orders p ON c.id = p.client_id
        WHERE p.id IS NULL;
    """
    print("Clients without movement:")
    print(pd.read_sql_query(query_c, conn))

    conn.close()
    
if __name__ == "__main__":
    local()
