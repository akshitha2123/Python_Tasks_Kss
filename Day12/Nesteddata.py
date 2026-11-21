# Nested Data Independence (Deep Copy)
import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

backup = copy.deepcopy(classes)

classes[0][1][0] = 50

print("Original Data:", classes)
print("Copied Data:", backup)
