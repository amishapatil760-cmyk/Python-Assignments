# Input
age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))

# Check
if age >= 18 and age <= 65 and weight >= 50:
    print("Eligible for Blood Donation")
else:
    print("Not Eligible for Blood Donation")