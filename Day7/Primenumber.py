# Write a program to check whether a number is Prime. Definition: A Prime number is a number that has only two factors

num = int(input("Enter a number: "))

factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors =", ", ".join(map(str, factors)))

if len(factors) == 2:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")