# Inventory Update System
# Concept: Adding values to a 2D array.

import numpy as np

inventory = np.array([
    [10, 15],
    [20, 25]
])

updated_inventory = inventory + 2

print("Original Inventory:")
print(inventory)

print("Updated Inventory:")
print(updated_inventory)
