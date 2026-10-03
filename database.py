import sqlite3

def init_db():
    conn = sqlite3.connect("finance_manager.db")
    cursor = conn.cursor()

    # users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    # transactions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    # Budgets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            month TEXT NOT NULL,  -- Format: YYYY-MM
            UNIQUE(user_id, category, month),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)


    conn.commit()
    conn.close()