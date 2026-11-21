# Random Matrix and Condition Filtering
import numpy as np

matrix = np.random.randint(0, 51, size=(3, 3))

print("Random Matrix:")
print(matrix)

result = matrix[matrix > 25]

print("Values Greater Than 25:", result)
