# Input 
year = int(input("Enter a year: "))

# century year
if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")

#  leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")