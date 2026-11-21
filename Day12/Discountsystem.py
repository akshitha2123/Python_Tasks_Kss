# Conditional Discount System (List Comprehension)
prices = [100, 200, 300, 400]

updated = [p * 0.9 if p > 200 else p for p in prices]

print("Original Prices:", prices)
print("Updated Prices:", updated)
