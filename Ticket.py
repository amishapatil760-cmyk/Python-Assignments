# Input:
age = int(input("Enter age: "))

# Check ticket category
if age < 12:
    print("Child Ticket")
elif age < 60:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")