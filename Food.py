# Display menu
print("1. idli")
print("2. dosa")
print("3. pohe")
print("4. Tea")

# Input choice
choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You selected idli")
    case 2:
        print("You selected dosa")
    case 3:
        print("You selected pohe")
    case 4:
        print("You selected tea")
    case _:
        print("Invalid Choice")