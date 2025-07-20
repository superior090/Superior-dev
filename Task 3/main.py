from budget_utils import Transaction, load_transactions, add_transaction, group_by_category, total_expenses
from datetime import datetime

def main():
    transactions = load_transactions()

    print("💰 Personal Budget Tracker")
    while True:
        print("\n1. Add Expense\n2. View Totals by Category\n3. View Total Expenses\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            try:
                datetime.strptime(date, "%Y-%m-%d")
                transaction = Transaction(date, category, amount)
                add_transaction(transactions, transaction)
                print(" Expense added.")
            except ValueError:
                print(" Invalid date format.")

        elif choice == "2":
            grouped = group_by_category(transactions)
            for cat, total in grouped.items():
                print(f"{cat}: ${total:.2f}")

        elif choice == "3":
            print(f"Total Expenses: ${total_expenses(transactions):.2f}")

        elif choice == "4":
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()