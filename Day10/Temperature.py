# 2D array and sum

import numpy as np

temperature = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

print("Temperature Data:")
print(temperature)

total = np.sum(temperature)

print("Total Temperature:", total)
