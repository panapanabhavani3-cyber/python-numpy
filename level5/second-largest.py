import numpy as np

a = np.array([10, 20, 30, 20, 40, 30])

unique = np.unique(a)
result = unique[-2]

print("Second-largest unique value:", result)