#  list the dictoinay


employees = [
    {"name": "Ravi", "age": 25, "salary": 30000},
    {"name": "Raju", "age": 30, "salary": 50000},
    {"name": "Ramu", "age": 28, "salary": 40000},
    {"name": "Mohan", "age": 35, "salary": 60000}
]

# Highest salary
highest = max(employees, key=lambda x: x["salary"])
print("Highest salary:", highest)
# Salary greater than 35000
filtered = []
for emp in employees:
    if emp["salary"] > 35000:
        filtered.append(emp)
print("Employees earning above 35000:", filtered)
# Average salary
total = 0
for emp in employees:
    total += emp["salary"]

average = total / len(employees)

print("Average salary:", average)
# Employee names
names = []
for emp in employees:
    names.append(emp["name"])
print("Employee names:", names)