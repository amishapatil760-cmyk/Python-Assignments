# Input:
ch = input("Enter a character: ")

# Check:
if ch.isupper():
    print("The character is Uppercase.")
elif ch.islower():
    print("The character is Lowercase.")
else:
    print("The input is not an alphabet.")