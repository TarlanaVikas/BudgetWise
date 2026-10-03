import sqlite3
from datetime import datetime

DB_NAME = "finance_manager.db"

def set_budget(user_id, category, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    month = datetime.now().strftime("%Y-%m")

    try:
        cursor.execute("""
            INSERT INTO budgets (user_id, category, amount, month)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id, category, month) DO UPDATE SET amount = excluded.amount
        """, (user_id, category, amount, month))
        conn.commit()
        print(f"Budget for {category} set to Rs.{amount} for {month}.")
    except Exception as e:
        print("Error setting budget:", e)
    finally:
        conn.close()

def check_budget(user_id, category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    month = datetime.now().strftime("%Y-%m")

    # Total expenses for the category this month
    cursor.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND category = ? AND type = 'expense'
        AND strftime('%Y-%m', date) = ?
    """, (user_id, category, month))
    spent = cursor.fetchone()[0] or 0.0

    # Budget for the category this month
    cursor.execute("""
        SELECT amount FROM budgets
        WHERE user_id = ? AND category = ? AND month = ?
    """, (user_id, category, month))
    budget = cursor.fetchone()

    conn.close()

    if budget:
        limit = budget[0]
        print(f"\nBudget Report for '{category}' ({month}):")
        print(f"Spent: Rs.{spent} / Budget: Rs.{limit}")
        if spent > limit:
            print("You have exceeded your budget!")
        else:
            print("You are within your budget.")
    else:
        print(f"No budget set for '{category}' in {month}.")
