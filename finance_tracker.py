finances= {}

choice = int(input("Welcome to the Personal Finance Tracker! Would you like to 1.Add expenses, 2.View All expenses, 3.View Summary, 4.Exit? "))

def add(category,description,amount):
    finances[category] = (description, amount)
    for category, (description, amount) in finances.items():
        print(f"Category: {category}, Description: {description}, Amount: ${amount}")

def view_expenses(data):
    print("Expenses:")
    for category, (description, amount) in finances.items():
        if data == category:
            print(f"Category: {category}, Amount: ${amount:.2f}, Description: {description}")
        elif data != category:
            print("Invalid Category, try adding a new expense")

def view_summary():
    print("Summary:")
    sum = 0
    for category, (description, amount) in finances.items():
         sum = sum + amount
    print(f"Category: {category}, Amount: ${sum}")

while choice != 4:
    if choice == 1:
            try:
                description = input("Enter expense description: ")
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                add(category,description,amount)
            except ValueError:
                print("Invalid value")

    elif choice == 2:
        try:
            data = input("Enter expense category to view total amount of expenses: ")
            view_expenses(data)
        except ValueError:
            print("Invalid value")

    elif choice == 3:
        view_summary()

    elif choice == 4:
        break

    choice = int(input(" Would you like to 1.Add expenses, 2.View All expenses, 3.View Summary, 4.Exit again? "))





