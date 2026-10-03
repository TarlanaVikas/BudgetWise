import unittest
from transactions import add_transaction, list_transactions
import sqlite3

class TestTransactions(unittest.TestCase):
    def test_add_transaction(self):
        user_id = 999
        add_transaction(user_id, 1000, "Test", "income", "Test income")
        conn = sqlite3.connect("finance_manager.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ? AND category = 'Test'", (user_id,))
        row = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(row)

if __name__ == '__main__':
    unittest.main()
