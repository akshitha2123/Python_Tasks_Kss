# Employee Bonus Calculator (Decorators & OOP)


def bonus(func):
    def wrapper(self):
        salary = func(self)
        final_salary = salary + 5000
        print("Original Salary:", salary)
        print("Bonus:", 5000)
        print("Final Salary:", final_salary)

    return wrapper

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display_salary(self):
        return self.salary

e = Employee("Akshitha", 30000)

print("Employee Name:", e.name)
e.display_salary()
