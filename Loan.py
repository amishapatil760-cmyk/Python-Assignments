# Input a
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))

# Check 
if age >= 18 and income >= 25000:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")