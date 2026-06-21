"""
Personal Budget Tracker
Final Project

This program lets a user add income, add expenses, view transactions,
view a spending summary, and save all data to a CSV file.
"""

import csv
from datetime import datetime

DATA_FILE = "budget_data.csv"


def load_transactions():
    """Load saved transactions from the CSV file."""
    transactions = []
    try:
        with open(DATA_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except FileNotFoundError:
        pass
    return transactions


def save_transactions(transactions):
    """Save all transactions to the CSV file."""
    with open(DATA_FILE, mode="w", newline="") as file:
        fieldnames = ["date", "type", "category", "description", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)


def add_income(transactions):
    """Add an income transaction."""
    category = input("Enter income category, such as Job or Gift: ")
    description = input("Enter a short description: ")

    try:
        amount = float(input("Enter income amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": "Income",
        "category": category,
        "description": description,
        "amount": amount,
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Income added successfully!")


def add_expense(transactions):
    """Add an expense transaction."""
    category = input("Enter expense category, such as Food, Rent, or Gas: ")
    description = input("Enter a short description: ")

    try:
        amount = float(input("Enter expense amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": "Expense",
        "category": category,
        "description": description,
        "amount": amount,
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Expense added successfully!")


def view_transactions(transactions):
    """Display all saved transactions."""
    if not transactions:
        print("No transactions have been added yet.")
        return

    print("\n--- All Transactions ---")
    for number, item in enumerate(transactions, start=1):
        print(
            f"{number}. {item['date']} | {item['type']} | "
            f"{item['category']} | {item['description']} | ${item['amount']:.2f}"
        )


def show_summary(transactions):
    """Show total income, total expenses, and current balance."""
    total_income = 0
    total_expenses = 0

    for item in transactions:
        if item["type"] == "Income":
            total_income += item["amount"]
        elif item["type"] == "Expense":
            total_expenses += item["amount"]

    balance = total_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance:        ${balance:.2f}")

    if balance < 0:
        print("Warning: You are spending more than you are earning.")
    elif balance == 0:
        print("Your income and expenses are exactly balanced.")
    else:
        print("Good job! You have money left in your budget.")


def show_menu():
    """Display the program menu."""
    print("\n===== Personal Budget Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Budget Summary")
    print("5. Exit")


def main():
    """Main function that controls the program."""
    transactions = load_transactions()

    while True:
        show_menu()
        choice = input("Choose an option from 1-5: ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            show_summary(transactions)
        elif choice == "5":
            print("Thank you for using the Personal Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
