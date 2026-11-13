#  Develop a Python program to manage student marks for three subjects. Store the subject 
# names in a tuple, maintain unique student names in a set, and store each student’s marks 
# in a list inside a dictionary where the key is the student name. Create user-defined 
# functions to add a student with marks, display all student records, and calculate the average 
# marks of a student. Implement a recursive function to calculate the total marks from the list of 
# marks. The program should interact with the user through a simple menu.


# Student Marks Management System
# Store subject names in a tuple
subjects = ("Math", "Science", "English")
# Store unique student names in a set
student_names = set()
# Store student marks in a dictionary
students = {}
# Recursive function to calculate total marks
def calculate_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + calculate_total(marks[1:])

# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists.")
            return
        marks = []

        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)

        student_names.add(name)
        students[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

# Function to display all students
def display_students():
    if not students:
        print("No student records found.")
        return
for name, marks in students.items():
        print(name, ":", marks)

# Function to calculate average marks
def calculate_average():
    try:
        name = input(
            "Enter student name to calculate average: "
        )

        if name not in students:
            raise NameError("Student not found")

        marks = students[name]

        if not isinstance(marks, list):
            raise TypeError("Marks must be stored in a list")

        total = calculate_total(marks)

        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")

# Main menu
while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again.")

    except ValueError:
        print("Please enter a valid menu number.")
