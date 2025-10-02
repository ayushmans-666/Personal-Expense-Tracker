# Smart Personal Expense Tracker
# Features:
# 1. Add income
# 2. Add expense
# 3. Show balance
# 4. Generate monthly report
# 5. Save data to file

import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

# File to store all data
DATA_FILE = "expenses.json"

# Load existing data or create new
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"income": [], "expenses": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add income
def add_income(data):
    try:
        amount = float(input("Enter income amount: "))
        note = input("Enter description (optional): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["income"].append({"amount": amount, "note": note, "date": date})
        save_data(data)
        print(f"Income of {amount} added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

# Add expense
def add_expense(data):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (Food, Travel, Bills, etc.): ")
        note = input("Enter description (optional): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["expenses"].append({"amount": amount, "category": category, "note": note, "date": date})
        save_data(data)
        print(f"Expense of {amount} added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

# Show current balance
def show_balance(data):
    total_income = sum(item["amount"] for item in data["income"])
    total_expense = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expense
    print("\n----- Current Balance -----")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}\n")

# Generate monthly report
def generate_report(data):
    month = input("Enter month (YYYY-MM): ")
    
    income_month = [item["amount"] for item in data["income"] if item["date"].startswith(month)]
    expense_month = [item["amount"] for item in data["expenses"] if item["date"].startswith(month)]
    
    total_income = sum(income_month)
    total_expense = sum(expense_month)
    balance = total_income - total_expense
    
    print(f"\n----- {month} Report -----")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}\n")
    
    # Pie chart for expense categories
    categories = {}
    for item in data["expenses"]:
        if item["date"].startswith(month):
            cat = item["category"]
            categories[cat] = categories.get(cat, 0) + item["amount"]
    
    if categories:
        plt.figure(figsize=(6,6))
        plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
        plt.title(f"Expense Distribution for {month}")
        plt.show()
    else:
        print("No expenses for this month to display chart.\n")

# Main menu
def main():
    data = load_data()
    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Generate Monthly Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            show_balance(data)
        elif choice == "4":
            generate_report(data)
        elif choice == "5":
            print("Thank you for using Smart Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
