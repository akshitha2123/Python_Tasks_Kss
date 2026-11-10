# . Write a program that uses random.choice() to randomly select a student from a 
# list and display: 
# "The selected student for presentation is: <name>". 

import random
students = ["Anu", "Ravi", "Priya", "Rahul", "Sneha"]
selected = random.choice(students)
print("The selected student for presentation is:", selected)