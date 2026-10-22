# ATM Menu
print("1. Balance ")
print("2. Cash Withdrawal")
print("3. Deposit")
print("4. Exit")

# Input choice
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Balance Enquiry ")
    case 2:
        print("Cash Withdrawal ")
    case 3:
        print("Deposit ")
    case 4:
        print("Thank You  Using ATM")
    case _:
        print("Invalid Choice")
