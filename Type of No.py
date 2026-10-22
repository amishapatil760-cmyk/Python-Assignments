# Input 
num = int(input("Enter a number: "))

num = abs(num)  # negative numbers handle

if num <= 9:
    print("Single Digit Number")
elif num <= 99:
    print("Double Digit Number")
elif num <= 999:
    print("Three Digit Number")
else:
    print("More than Three Digits")