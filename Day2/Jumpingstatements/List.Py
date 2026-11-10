# Write a program that searches for a number in a list and breaks the loop when found

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter a number to search: "))

for i in numbers:
    if i == search:
        print("Number found:", i)
        break
else:
    print("Number not found")