#  Write a program to check whether a given number is a Strong number. Definition: A Strong number is a number whose sum of factorial of digits is equal to the number itself

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong(n):
    total = 0
    temp = n
    while temp > 0:
        total += factorial(temp % 10)
        temp //= 10
    return total == n

num = int(input("Enter a number: "))
if is_strong(num):
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")