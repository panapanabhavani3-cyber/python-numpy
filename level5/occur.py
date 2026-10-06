import numpy as np

a = np.array([1, 2, 3, 2, 4, 3, 5])

unique, counts = np.unique(a, return_counts=True)
result = unique[counts == 1]

print("Values occurring once:", result)