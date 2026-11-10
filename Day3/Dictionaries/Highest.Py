# Find the student with the highest marks from a dictionary

students = {
    "Akash": 85,
    "Ravi": 90,
    "Priya": 95
}

highest_student = max(students, key=students.get)
print("Student with highest marks:", highest_student)
print("Highest marks:", students[highest_student])