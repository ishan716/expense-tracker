import sqlite3

# Initialize Database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
                  id INTEGER PRIMARY KEY, 
                  date TEXT, 
                  category TEXT, 
                  amount REAL)""")
conn.commit()

# Add Expense
def add_expense(date, category, amount):
    cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", 
                   (date, category, amount))
    conn.commit()
    print("Expense added!")

# View Expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    for row in cursor.fetchall():
        print(row)

# Main Menu
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(date, category, amount)
    elif choice == "2":
        print("\nExpenses:")
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Try again.")

conn.close()
