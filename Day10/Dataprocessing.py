# . Data Processing Pipeline
# Concept: Sorting, splitting, and sum.

import numpy as np

data = [12, 7, 25, 3, 18, 10]

arr = np.array(data)

sorted_array = np.sort(arr)

parts = np.split(sorted_array, 2)

sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

print("Sorted Array:", sorted_array)

print("First Split:", parts[0])
print("Second Split:", parts[1])

print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)
