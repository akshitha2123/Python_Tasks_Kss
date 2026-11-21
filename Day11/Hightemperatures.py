# Filter High Temperature Values
# Concept: Boolean filtering
import numpy as np

temperature = np.array([28, 31, 35, 27, 40, 22])

result = temperature[temperature > 30]

print("Temperatures Above 30:", result)
