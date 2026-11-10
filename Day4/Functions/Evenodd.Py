#  Check whether a number is even or odd using a function

def check_number(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

n = int(input("Enter a number: "))

check_number(n)