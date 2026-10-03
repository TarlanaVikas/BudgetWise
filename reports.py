import sqlite3
from datetime import datetime

DB_NAME = "finance_manager.db"

def generate_monthly_report(user_id, year, month):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, SUM(amount) 
        FROM transactions 
        WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY type
    """, (user_id, str(year), str(month).zfill(2)))

    result = dict(cursor.fetchall())

    income = result.get("income", 0.0)
    expense = result.get("expense", 0.0)
    savings = income - expense

    print(f"\n--- Monthly Report for {year}-{str(month).zfill(2)} ---")
    print(f"Total Income : {income}")
    print(f"Total Expenses : {expense}")
    print(f"Total Savings : {savings}")

    conn.close()

def generate_yearly_report(user_id, year):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, SUM(amount) 
        FROM transactions 
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY type
    """, (user_id, str(year)))

    result = dict(cursor.fetchall())

    income = result.get("income", 0.0)
    expense = result.get("expense", 0.0)
    savings = income - expense

    print(f"\n--- Yearly Report for {year} ---")
    print(f"Total Income : {income}")
    print(f"Total Expenses : {expense}")
    print(f"Total Savings : {savings}")

    conn.close()
