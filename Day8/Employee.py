file = open("employees.txt", "a")
name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))
file.write(name + " " + str(salary) + "\n")
file.close()
print("Employee details saved successfully!")
file = open("employees.txt", "r")
employees = []
print("Employee Details:")
for line in file:
 name, salary = line.split()
salary = int(salary)
print(name, salary)
employees.append((name, salary))
file.close()
if len(employees) > 0:
    highest = max(employees, key=lambda x: x[1])
    print("Highest Salary Employee:", highest[0])
    print("Highest Salary:", highest[1])
else:
    print("No employee records found")
