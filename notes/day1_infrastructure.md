# Day 1: Data Engineering Infrastructure & Environment Setup
**Date:** April 6, 2026  
**Engineer:** Nishant (Data Engineer)  
**Project:** DE_Mastery_2026 (Local Folder: `~/DE`)

---

## 1. Operating System & Terminal Setup
We initialized a **WSL 2 (Windows Subsystem for Linux)** instance running **Ubuntu 24.04**. This provides a native Linux kernel required for professional Data Engineering tools.

### **Core Commands Executed:**
* `sudo apt update && sudo apt upgrade -y`
* `mkdir ~/DE`
* `mv ~/DE_Mastery_2026 ~/DE` (Folder refactor)

---

## 2. Python Environment (The "Clean Room")
To avoid the `externally-managed-environment` error, we implemented a **Virtual Environment**.

### **Setup Workflow:**
1. **Install venv:** `sudo apt install python3-venv -y`
2. **Create Env:** `python3 -m venv .venv`
3. **Activate:** `source .venv/bin/activate`
4. **Install Dependencies:** `pip install psycopg2-binary`



---

## 3. Database Layer: PostgreSQL 16
### **Configuration:**
* **Service:** `sudo service postgresql start`
* **DB Instance:** `de_practice`
* **Password:** `admin123`
### **Schema Definition (DDL):**
```sql
CREATE TABLE IF NOT EXISTS watch_inventory (
    id SERIAL PRIMARY KEY,
    brand TEXT,
    model TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 4. Version Control: GitHub (`nishant-iiitb/DE`)
Connected the local workstation to the cloud portfolio using secure authentication.

### **Key Configurations:**
* **Identity:** 
    * `git config --global user.name "Nishant"`
    * `git config --global user.email "nishant-iiitb@example.com"`
* **Auth Automation:** `git config --global credential.helper store` (Saves the Personal Access Token for 30 days).
* **Ignored Files (.gitignore):** Hiding `.venv/`, `__pycache__/`, and `.pyc` from the cloud to maintain repository hygiene.

---

## 5. The Final Working Code (`day1_load.py`)
This is the "Golden Copy" of our first ETL script. It handles connection, table creation, and batch loading using a context manager.

```python
import psycopg2

def load_data():
    watches = [('Casio', 'Edifice'), ('G-Shock', 'GA-2100'), ('Seiko', '5 Sports')]

    try:
        # Explicit connection with Password Auth
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="de_practice",
            user="postgres",
            password="admin123"
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Ensure Table Exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS watch_inventory (
                id SERIAL PRIMARY KEY,
                brand TEXT,
                model TEXT
            );
        """)

        # Perform Batch Load
        query = "INSERT INTO watch_inventory (brand, model) VALUES (%s, %s)"
        cur.executemany(query, watches)
        
        print(f"✔ Successfully loaded {len(watches)} records into SQL.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"✖ Database Error: {e}")

if __name__ == "__main__":
    load_data()
```

## 6. Troubleshooting Log (Crucial Fixes)

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **Relation doesn't exist** | Table not committed | Added `CREATE TABLE IF NOT EXISTS` and `autocommit=True`. |
| **fe_sendauth failed** | Password missing | Set DB password to `admin123` and updated script. |
| **Pip Error** | System Python Protection | Created and activated `.venv`. |
| **Git Password Prompt** | Credential cache off | Ran `git config --global credential.helper store`. |

---
**End of Day 1 Ledger.**