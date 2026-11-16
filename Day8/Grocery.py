file = open("grocery.txt", "w")
n = int(input("How many items? "))
for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")
file.close()
print("Grocery items saved successfully!")
file = open("grocery.txt", "r")
print("Grocery List:")
for item in file:
    print(item.strip())
file.close()
file = open("marks.txt", "r")
total = 0
count = 0
print("Student Records:")
for line in file:
    name, marks = line.split()
marks = int(marks)
print(name, marks)
total = total + marks
count = count + 1
file.close()
if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No student records found")
