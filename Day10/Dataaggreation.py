# Multi-Department Data Aggregation
# Concept: Matrix concatenation and sum.

import numpy as np

branchA = np.array([
    [10, 20],
    [30, 40]
])

branchB = np.array([
    [5, 15],
    [25, 35]
])

combined = np.concatenate((branchA, branchB))

total = np.sum(combined)

print("Combined Matrix:")
print(combined)

print("Total Employees:", total)
