# Write a program to reverse a string without using built-in reverse functions

text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reversed string:", reverse)