# Write a program to check whether a given number is an Armstrong number or not. Definition: A number is called an Armstrong number if the sum of the cubes of its digits is equal to the number

def is_armstrong(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")