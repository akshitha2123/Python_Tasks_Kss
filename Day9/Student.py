# Student Information System (Class & Object)
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print()

s1 = Student("Akshitha", 101, 90)
s2 = Student("Priya", 102, 85)
s3 = Student("Rahul", 103, 88)

s1.display()
s2.display()
s3.display()
