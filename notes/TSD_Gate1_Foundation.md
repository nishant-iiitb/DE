## 📝 TSD: Gate 1 - SQL Foundations & Python Connectivity
**Project ID:** DE-G1-01 

**Status:** In-Progress

**Objective:** Establish a resilient connection between Python and MySQL and demonstrate mastery of "Senior Filter" SQL logic (WHERE vs. HAVING).

--------------
### 🏗️ 1. System Architecture
The solution follows a standard Local ETL pattern:

- **Language:** Python 3.12
- **Database:** MySQL 8.0
- **Bridge:** mysql-connector-python
- **Environment:** WSL 2 (Ubuntu 24.04)

---------
### 📊 2. Data Modeling (Proof of Concept)
We will model a `watch_sales` table to demonstrate row-level vs. group-level filtering.

**Table Schema:** `watch_sales`
| Column | Data Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| sale_id | INT | PRIMARY KEY | Unique transaction ID |
| brand | VARCHAR(50) | NOT NULL | Watch Brand (e.g., Casio, Seiko) |
| model | VARCHAR(100) | NOT NULL | Model Name |
| price | DECIMAL(10,2) | NOT NULL | Sale Price |
| sale_date | DATE | NOT NULL | Date of Transaction |
-----------
### 🛠️ 3. Logical Execution Plan
1. **Handshake:** Establish a secure connection to the de_practice database using credentials.
2. **DDL Execution:** Create the watch_sales table.
3. **DML Execution:** Insert sample records covering different price points and brands.
4. **The Logic Test:**
    - **WHERE Query:** Filter rows where price > 500 (Filters before aggregation).
    - **HAVING Query:** Group by brand and filter where SUM(price) > 5000 (Filters after aggregation).
------
### ⚠️ 4. Failure Modes & Handling
- **Auth Error:** Handled via mysql.connector.Error.
- **Data Integrity:** Use TRUNCATE at the start of the script to ensure a clean state for testing.