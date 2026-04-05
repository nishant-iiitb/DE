import psycopg2

def load_data():
    watches = [('Casio', 'Edifice'), ('G-Shock', 'GA-2100'), ('Seiko', '5 Sports')]

    try:
        # 1. Connect explicitly
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="de_practice",
            user="postgres",
            password="admin123"
        )
        # 2. Enable Autocommit for Day 1 debugging
        conn.autocommit = True
        cur = conn.cursor()

        print("--- Connected to Database ---")

        # 3. Create Table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS watch_inventory (
                id SERIAL PRIMARY KEY,
                brand TEXT,
                model TEXT
            );
        """)
        print("--- Table Checked/Created ---")

        # 4. Insert Data
        for brand, model in watches:
            cur.execute("INSERT INTO watch_inventory (brand, model) VALUES (%s, %s)", (brand, model))
        
        print(f"--- Successfully loaded {len(watches)} records ---")

        # 5. Close
        cur.close()
        conn.close()

    except Exception as e:
        print(f"✖ Database Error: {e}")

if __name__ == "__main__":
    load_data()