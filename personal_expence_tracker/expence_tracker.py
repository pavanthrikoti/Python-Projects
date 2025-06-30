import json
import os
from datetime import datetime

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses, amount, category, description):
    expenses.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": float(amount),
        "category": category,
        "description": description
    })
    print(f"Expense added: ₹{amount:.2f} for {description} ({category})")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nYour Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['date']} - ₹{expense['amount']:.2f} - {expense['category']} - {expense['description']}")

def view_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        summary[category] = summary.get(category, 0) + amount
    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

def delete_expense(expenses, index):
    if 1 <= index <= len(expenses):
        removed_expense = expenses.pop(index-1)
        print(f"Expense deleted: ₹{removed_expense['amount']:.2f} - {removed_expense['description']}")
    else:
        print("Invalid expense number.")

def main():
    expenses = load_expenses()
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary by Category")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g., Food, Transport, Bills): ")
                description = input("Enter description: ")
                if amount > 0 and category.strip() and description.strip():
                    add_expense(expenses, amount, category, description)
                    save_expenses(expenses)
                else:
                    print("Invalid input. Amount must be positive and fields cannot be empty.")
            except ValueError:
                print("Please enter a valid number for amount.")
                
        elif choice == "2":
            view_expenses(expenses)
            
        elif choice == "3":
            view_summary(expenses)
            
        elif choice == "4":
            view_expenses(expenses)
            try:
                index = int(input("Enter expense number to delete: "))
                delete_expense(expenses, index)
                save_expenses(expenses)
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()