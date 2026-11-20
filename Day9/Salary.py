# Employee Salary System (Simple Inheritance)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

m1 = Manager("Akshitha", 30000)
m1.display()
