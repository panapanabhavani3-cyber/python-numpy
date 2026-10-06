import numpy as np

a = np.array([1, 2, 2, 3, 3, 3, 4])

values, counts = np.unique(a, return_counts=True)

for value, count in zip(values, counts):
    print(value, ":", count)