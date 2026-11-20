#Splitting Data for Parallel Processing
#Concept: NumPy split.

import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

parts = np.split(data, 3)

print("Original Array:", data)

print("Part 1:", parts[0])
print("Part 2:", parts[1])
print("Part 3:", parts[2])
