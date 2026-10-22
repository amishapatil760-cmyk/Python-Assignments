# Input 
username = input("Enter username: ")
password = input("Enter password: ")

# Nested if loop
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")