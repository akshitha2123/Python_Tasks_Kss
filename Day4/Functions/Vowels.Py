# Write a function that takes a string as input and returns the number of vowels

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

name = input("Enter a string: ")

print("Number of vowels:", count_vowels(name))