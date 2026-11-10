# Count the frequency of each character in a string

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:", frequency)