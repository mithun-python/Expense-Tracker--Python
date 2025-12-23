# Expense Tracker System
# Author: Mithun
# Description: Simple file-based expense tracker using Python

import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file with headers if not exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass

# Add new expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/etc): ")
    amount = input("Enter amount: ")
    note = input("Enter note: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Calculate total expense
def total_expense():
    total = 0
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])
    print("💰 Total Expense:", total)

# Main menu
def menu():
    initialize_file()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("❌ Invalid choice")

menu()
