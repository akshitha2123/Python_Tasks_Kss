# Copy vs View Behavior in Data Processing
# Concept: copy() and view()

import numpy as np

# Copy example
arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

arr[0] = 100

print("Original Array:", arr)
print("Copy Array:", copy_arr)

# View example
arr2 = np.array([10, 20, 30, 40])

view_arr = arr2.view()

arr2[0] = 100

print("Original Array:", arr2)
print("View Array:", view_arr)
