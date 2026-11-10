#  Given a string `"programming"`, create a dictionary that counts how many times each character appears

text = "programming"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)