# Input:
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

# Calculate:
if years > 5:
    bonus = salary * 0.10
elif years >= 3:
    bonus = salary * 0.05
else:
    bonus = 0

print("Bonus =", bonus)