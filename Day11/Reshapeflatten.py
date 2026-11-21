# Reshape and Flatten Image Data
# Concept: flatten()
import numpy as np

image = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = image.flatten()

print("Original Matrix:")
print(image)

print("Flattened Array:")
print(result)
