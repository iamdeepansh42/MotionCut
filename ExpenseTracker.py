import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expense_data = []

    def add_expense(self, amount, description, category):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expense_entry = {"timestamp": timestamp, "amount": amount, "description": description, "category": category}
        self.expense_data.append(expense_entry)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expense_data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.expense_data = json.load(file)
        except FileNotFoundError:
            pass

    def view_monthly_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expense_data if
                            datetime.strptime(expense["timestamp"], "%Y-%m-%d %H:%M:%S").month == month
                            and datetime.strptime(expense["timestamp"], "%Y-%m-%d %H:%M:%S").year == year]
        total_expenses = sum(expense["amount"] for expense in monthly_expenses)

        print(f"\nMonthly Summary ({month}/{year}):")
        print(f"Total Expenses: Rs{total_expenses:.2f}")

        categories = set(expense["category"] for expense in monthly_expenses)
        for category in categories:
            category_expenses = [expense["amount"] for expense in monthly_expenses if expense["category"] == category]
            category_total = sum(category_expenses)
            print(f"{category.capitalize()}: Rs{category_total:.2f}")

    def display_categories(self):
        categories = set(expense["category"] for expense in self.expense_data)
        print("\nExpense Categories:")
        for category in categories:
            print(f"- {category.capitalize()}")

# Example Usage
tracker = ExpenseTracker()
tracker.load_from_file("expenses.json")

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. Display Categories")
    print("4. Save and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter the amount spent: Rupees "))
        description = input("Enter a brief description: ")
        category = input("Enter the expense category: ")
        tracker.add_expense(amount, description, category)

    elif choice == "2":
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year: "))
        tracker.view_monthly_summary(month, year)

    elif choice == "3":
        tracker.display_categories()

    elif choice == "4":
        tracker.save_to_file("expenses.json")
        print("Expense data saved. Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")