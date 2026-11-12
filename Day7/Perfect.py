#  Write a program to check whether a number is a Perfect number. Definition: A Perfect number is a number whose sum of proper divisors equals the number

def get_proper_divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def is_perfect(n):
    if n < 2:
        return False
    return sum(get_proper_divisors(n)) == n

num = int(input("Enter a number: "))

if num > 1:
    divisors = get_proper_divisors(num)
    print("Divisors:", ", ".join(map(str, divisors)))
    print("Sum =", " + ".join(map(str, divisors)), "=", sum(divisors))

if is_perfect(num):
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")