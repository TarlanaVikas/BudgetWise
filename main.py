from database import init_db
from authen import register_user, login_user
from transactions import add_transaction, list_transactions
from reports import generate_monthly_report, generate_yearly_report
from budget import set_budget, check_budget
from backup import backup_data, restore_data

def user_dashboard(user_id):
    while True:
        print("\n--- Finance Dashboard ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Monthly Report")
        print("4. Yearly Report")
        print("5. View All Transactions")
        print("6. Set Budget")
        print("7. Check Budget")
        print("8. Logout")
        
        choice = input("Select an option: ")

        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category (e.g., Salary,Stocks): ")
            description = input("Description (optional): ")
            add_transaction(user_id, amount, category, 'income', description)

        elif choice == '2':
            amount = float(input("Amount: "))
            category = input("Category (e.g., Food): ")
            description = input("Description (optional): ")
            add_transaction(user_id, amount, category, 'expense', description)
            
        elif choice == '3':
            year = input("Enter year (YYYY): ")
            month = input("Enter month (1-12): ")
            generate_monthly_report(user_id, year, month)

        elif choice == '4':
            year = input("Enter year (YYYY): ")
            generate_yearly_report(user_id, year)

        elif choice == '5':
            list_transactions(user_id)
        
        elif choice == '6':
            category = input("Enter category (e.g., Food): ")
            amount = float(input("Enter budget amount: "))
            set_budget(user_id, category, amount)

        elif choice == '7':
            category = input("Enter category to check: ")
            check_budget(user_id, category)

        elif choice == '8':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Register")
        print("2. Login")
        print("3. Backup Data")
        print("4. Restore Data")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_id = login_user(username, password)
            if user_id:
                print(f"Welcome, {username}!")
                user_dashboard(user_id)
            
        elif choice == '3':
            backup_data()

        elif choice == '4':
            restore_data()
                
                
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    init_db()
    main_menu()
    