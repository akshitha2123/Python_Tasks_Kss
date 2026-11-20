# Shape Area Calculator (Polymorphism)


import math

class Circle:
    def area(self):
        print("Circle Area:", round(math.pi * 5 * 5, 2))

class Rectangle:
    def area(self):
        print("Rectangle Area:", 10 * 5)

class Triangle:
    def area(self):
        print("Triangle Area:", 0.5 * 10 * 6)

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()
