from utilities import math_operations, string_operations

print("Addition:", math_operations.add(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))

text = input("Enter a string: ")
print("Uppercase:", string_operations.to_upper(text))
print("Character count:", string_operations.count_characters(text))
