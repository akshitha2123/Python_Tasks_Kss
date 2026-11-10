#  Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details

students = {
    "vakul": 85,
    "Anil": 90,
    "aksha": 78
}

students["Sneha"] = 95

students["vakul"] = 92

for name, marks in students.items():
    print(name, ":", marks)