expenses = []

while True:
    user_input = input("Enter an expense (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break
    

    try:
        expense = float(user_input)
        expenses.append(expense)
    except ValueError:
        print("Please enter a valid number.")

if expenses:
    print("\nExpense Summary:")
    print("--------------------")
    print(f"Number of expenses: {len(expenses)}")
    print(f'Total: ${sum(expenses):.2f}')
    print(f'Average: ${sum(expenses) / len(expenses):.2f}')
    print(f'Highest Expense: ${max(expenses):.2f}')
    print(f'Lowest Expense: ${min(expenses):.2f}')
else:
    print("No expenses were entered.")

