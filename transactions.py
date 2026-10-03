import sqlite3
from datetime import datetime

DB_NAME = "finance_manager.db"

def add_transaction(user_id, amount, category, trans_type, description=""):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO transactions (user_id, amount, category, date, type, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, amount, category, date, trans_type, description))

    conn.commit()
    conn.close()
    print(f"{trans_type.capitalize()} added successfully.")

def list_transactions(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, date, type, category, amount, description
        FROM transactions
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,))

    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No transactions found.")
        return

    print("\n--- Your Transactions ---")
    for row in results:
        print(f"[{row[0]}] {row[1]} | {row[2].capitalize()} | {row[3]} | ₹{row[4]} | {row[5]}")
