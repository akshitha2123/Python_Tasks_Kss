# Boolean Masking for Salary Analysis
import numpy as np

salary = np.array([25000, 40000, 15000, 50000, 30000])

result = salary[salary > 30000]

count = np.sum(salary > 30000)

print("Salaries Above 30000:", result)
print("Number of Employees:", count)
