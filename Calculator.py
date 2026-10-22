# Input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Choose 
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case "/":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero is not possible")
    case _:
        print("Invalid Operator")