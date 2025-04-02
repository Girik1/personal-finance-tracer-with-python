import csv
import datetime

def load_transactions(filename="transactions.csv"):
    """Loads transactions from a CSV file."""
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            transactions = []
            for row in reader:
                transactions.append({
                    "date": datetime.datetime.strptime(row[0], "%Y-%m-%d").date(),
                    "description": row[1],
                    "amount": float(row[2])
                })
            return transactions
    except FileNotFoundError:
        return []

def save_transactions(transactions, filename="transactions.csv"):
    """Saves transactions to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Amount"])
        for transaction in transactions:
            writer.writerow([
                transaction["date"].strftime("%Y-%m-%d"),
                transaction["description"],
                transaction["amount"]
            ])

def add_transaction(transactions, description, amount):
    """Adds a new transaction."""
    date = datetime.date.today()
    transactions.append({"date": date, "description": description, "amount": amount})
    print("Transaction added successfully.")

def calculate_balance(transactions):
    """Calculates the current balance."""
    balance = 0
    for transaction in transactions:
        balance += transaction["amount"]
    return balance

def view_transactions(transactions):
    """Displays all transactions."""
    if not transactions:
        print("No transactions found.")
        return

    print("\nTransaction History:")
    print("-" * 40)
    for transaction in transactions:
        print(f"{transaction['date']}: {transaction['description']} - ${transaction['amount']:.2f}")
    print("-" * 40)

def main():
    """Main function to run the finance tracker."""
    transactions = load_transactions()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter income description: ")
            amount = float(input("Enter income amount: "))
            add_transaction(transactions, description, amount)
        elif choice == "2":
            description = input("Enter expense description: ")
            amount = -float(input("Enter expense amount: ")) #expenses are negative
            add_transaction(transactions, description, amount)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            balance = calculate_balance(transactions)
            print(f"Current Balance: ${balance:.2f}")
        elif choice == "5":
            save_transactions(transactions)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()