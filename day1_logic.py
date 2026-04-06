import mysql.connector
from mysql.connector import Error

def run_foundation_test():
    conn = None
    try:
        # 1. The Handshake: Establising Connection
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='de_practice'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            print("Successfully connected to MySQL")

            # 2. DDL: Create a clean table for the test
            cursor.execute("""
                CREATE TABLE watch_sales (
                    sale_id INT AUTO_INCREMENT PRIMARY KEY,
                    brand VARCHAR(50),
                    model VARCHAR(100),
                    price DECIMAL(10,2),
                    sale_date DATE
                );
            """)

            # 3. DML: Bulk insert dummy data
            sql_insert = "INSERT INTO watch_sales (brand, model, price, sale_date) VALUES (%s, %s, %s, %s)"
            val = [
                ('Casio', 'Edifice', 12000, '2026-04-01'),
                ('Casio', 'G-Shock', 8000, '2026-04-02'),
                ('Seiko', '5 Sports', 25000, '2026-04-03'),
                ('Seiko', 'Presage', 45000, '2026-04-04'),
                ('Titan', 'Edge', 15000, '2026-04-05'),
                ('Casio', 'Vintage', 3000, '2026-04-06')
            ]
            cursor.executemany(sql_insert, val)
            conn.commit()
            print(f"{cursor.rowcount} records inserted successfully.\n")

            # 4. Logic Test: WHERE (Row-level filter)
            # This happens BEFORE grouping
            print("--- TEST 1: WHERE Clause (Price > 10,000) ---")
            cursor.execute("SELECT * FROM watch_sales WHERE price > 10000")
            for row in cursor.fetchall():
                print(row)

            # 5. Logic Test: HAVING (Group-level filter)
            # This happens AFTER grouping/aggregation
            print("\n--- TEST 2: HAVING Clause (Total Brand Revenue > 20,000) ---")
            cursor.execute("""
                SELECT brand, SUM(price) as total_revenue 
                FROM watch_sales 
                GROUP BY brand 
                HAVING total_revenue > 20000
            """)
            for row in cursor.fetchall():
                print(row)

    except Error as e:
        print(f"Database Error: {e}")
    finally:
        # Crucial for Data Engineers: Always close connections to avoid memory leaks
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("\nMySQL connection closed.")

if __name__ == "__main__":
    run_foundation_test()
