# Random Dataset Normalization + Filtering
import numpy as np

arr = np.random.rand(8)

print("Original Values:", arr)

normalized = arr * 100

print("Normalized Values:", normalized)

filtered = normalized[normalized > 50]

print("Filtered Values:", filtered)

sorted_values = np.sort(filtered)

print("Sorted Values:", sorted_values)
