# Convert Float Prices to Integer
# Concept: astype()
import numpy as np

prices = np.array([10.5, 20.8, 15.3])

new_prices = prices.astype(int)

print("Original Prices:", prices)
print("Integer Prices:", new_prices)
