#Expense Tracker Project

print("Welcome to our Expense tracker project")
expensesList = [] #List of expenses in the form of dictionary

while True:
    print("---MENU---")
    print("1) Add Expense")
    print("2) View Expense history")
    print("3) View Total Expense")
    print("4) Exit")

    choice = int(input("Enter your request no: "))

#Add Expense

    if(choice == 1):
        date = input("Enter the expense date (DD/MM/YY): ")
        category = input("Enter the expense category: ")
        description = input("Enter description about your expense: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date" : date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print("Your Expense is added succesfully \n")

#View Expense History

    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No expenses added \n")
        else:
            print("Your expenses are: ")
            count = 1
            for i in expensesList:
                print(f"Expense number {count} --> {i["date"]}, {i["category"]}, {i["description"]}, {i["amount"]}")
                count = count + 1

#View Total Expense

    elif(choice == 3):

        total = 0
        for i in expensesList:
            total = total + i["amount"]
        print("\nYour total expense is: ", total)

#Exit

    elif(choice == 4):
        print("\n Thank you for using our system")
        break

    else:
        print("Chodna naki vai? Choose from 1 to 4")