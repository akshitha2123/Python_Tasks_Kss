# Multi-Level List Transformation (Advanced List Comprehension)

data = [[1, 2, 3], [4, 5], [6]]

flat = [x for sublist in data for x in sublist]

squares = [x**2 for x in flat if x % 2 == 0]

print("Flattened List:", flat)
print("Even Number Squares:", squares)
