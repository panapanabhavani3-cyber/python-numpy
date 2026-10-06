import numpy as np

a = np.array([10, 50, 20, 40, 30])

third = np.partition(a, -3)[-3]

print("Third-largest value:", third)