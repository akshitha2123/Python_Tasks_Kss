# Assign grades based on marks

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 0:
    print("Fail")
else:
    print("Invalid marks")