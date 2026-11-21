# Employee Data Copy Issue (Shallow vs Deep Copy)
import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

shallow = copy.copy(employees)

employees[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow)

deep = copy.deepcopy(employees)

employees[0][1] = "X"

print("Original After Change:", employees)
print("Deep Copy:", deep)
