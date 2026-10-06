import numpy as np

a = np.array([10, 50, 20, 80, 30, 70])

indexes = np.argsort(a)[-3:][::-1]
values = a[indexes]

print("Top 3 values:", values)
print("Indexes:", indexes)