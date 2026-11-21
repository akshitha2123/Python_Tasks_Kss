# Find Indexes of Specific Value
# Concept: where()
import numpy as np

defects = np.array([2, 4, 1, 4, 3, 4, 5])

result = np.where(defects == 4)

print("Indexes:", result[0])
