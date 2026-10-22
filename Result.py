# Input 
status = input("Enter result status (P/F/D): ").upper()

match status:
    case "P":
        print("Pass")
    case "F":
        print("Fail")
    case "D":
        print("Distinction")
    case _:
        print("Invalid Status")