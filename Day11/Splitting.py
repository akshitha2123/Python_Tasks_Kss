# Splitting Student Scores Across Servers
Concept: array_split()
import numpy as np

scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])

result = np.array_split(scores, 4)

print("Server 1:", result[0])
print("Server 2:", result[1])
print("Server 3:", result[2])
print("Server 4:", result[3])
