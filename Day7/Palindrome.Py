# Palindrome Number Question: Write a program to check whether a number is a Palindrome

def is_palindrome(n):
    reverse = 0
    temp = n
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
    return reverse == n

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")