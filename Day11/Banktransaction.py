# Bank Transaction Storage
# Concept: NumPy array, type(), isinstance()
import numpy as np

transactions = [1200, 500, 800, 1500]

arr = np.array(transactions)

print("Array:", arr)
print("Type:", type(arr))
print("Is NumPy Array:", isinstance(arr, np.ndarray))
