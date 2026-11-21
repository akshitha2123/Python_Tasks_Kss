# Random Sales Simulation (NumPy)
import numpy as np

sales = np.random.randint(100, 501, size=10)

print("Daily Sales:", sales)
print("Average Sales:", np.mean(sales))
