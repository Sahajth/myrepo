from data_handler import add_expense, load_expenses_from_csv, save_expenses_to_csv, get_monthly_summary
from visualization import visualize_expenses

expenses = load_expenses_from_csv()

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Visualize Expenses")
        print("4. Export Data to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            add_expense(expenses, amount, date, category, description)

        elif choice == '2':
            month = int(input("Enter month (MM): "))
            year = int(input("Enter year (YYYY): "))
            summary = get_monthly_summary(expenses, month, year)
            print(summary)

        elif choice == '3':
            visualize_expenses(expenses)

        elif choice == '4':
            save_expenses_to_csv(expenses)
            print("Data exported to expenses.csv")

        elif choice == '5':
            save_expenses_to_csv(expenses)
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()