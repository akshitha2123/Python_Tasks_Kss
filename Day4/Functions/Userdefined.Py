# Find the sum of list elements using a user-defined function

def find_sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

my_list = [10, 20, 30, 40, 50]

print("Sum of elements:", find_sum(my_list))