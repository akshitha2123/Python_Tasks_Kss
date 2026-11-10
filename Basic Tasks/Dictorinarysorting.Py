# Given a dictionary Python

students = {
    "Vakul": 85,
    "shash": 92,
    "yousf": 78,
    "Rama": 95
}
sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)
print("Sorted students:")
for name, marks in sorted_students:
    print(name, ":", marks)
print("Top two students:")
for name, marks in sorted_students[:2]:
    print(name, ":", marks)