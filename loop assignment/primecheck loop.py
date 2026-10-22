num = int(input("Enter a number: "))

i = 2
prime = True

if num <= 1:
    prime = False
else:
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")