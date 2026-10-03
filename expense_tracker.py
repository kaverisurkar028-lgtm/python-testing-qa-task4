import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self):
        try:
            category = input("Enter Category: ")
            amount = float(input("Enter Amount: "))
            desc = input("Enter Description: ")
            date = datetime.now().strftime("%Y-%m-%d")
            expense = {"category": category, "amount": amount, "description": desc, "date": date}
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense Added Successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found!")
            return
        total = 0
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp['date']} | {exp['category']} | Rs.{exp['amount']} | {exp['description']}")
            total += exp['amount']
        print(f"\nTotal Spent: Rs.{total}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose: ")
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")
