# Input 
attendance = int(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

# Check 
if attendance >= 75:
    if marks >= 40:
        print("Eligible for Exam")
    else:
        print("Not Eligible (Low Marks)")
else:
    print("Not Eligible (Low Attendance)")