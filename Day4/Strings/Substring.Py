# Check whether a substring exists in a string

text = input("Enter a string: ")
sub = input("Enter substring to search: ")

if sub in text:
    print("Substring exists")
else:
    print("Substring does not exist")