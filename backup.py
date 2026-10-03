import shutil
import os

DB_NAME = "finance_manager.db"
BACKUP_FILE = "finance_backup.db"

def backup_data():
    if os.path.exists(DB_NAME):
        shutil.copyfile(DB_NAME, BACKUP_FILE)
        print(f"Backup created as '{BACKUP_FILE}'.")
    else:
        print("Database file not found.")

def restore_data():
    if os.path.exists(BACKUP_FILE):
        shutil.copyfile(BACKUP_FILE, DB_NAME)
        print("Data restored from backup.")
    else:
        print("Backup file not found.")
