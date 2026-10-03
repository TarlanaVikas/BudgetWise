import sqlite3
from utils import hash_password, verify_password

DB_NAME = "finance_manager.db"

def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        hashed = hash_password(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        print("Registration successful.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        user_id, stored_password = result
        if verify_password(password, stored_password):
            print("Login successful.")
            return user_id  
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
    
    return None