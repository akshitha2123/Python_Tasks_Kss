#  iven a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List without duplicates:", unique)