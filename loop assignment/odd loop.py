num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        sum = sum + digit

    num = num // 10

print("Sum of odd digits =", sum)