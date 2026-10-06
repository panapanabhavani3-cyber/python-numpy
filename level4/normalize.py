import numpy as np

a = np.array([10, 20, 30, 40, 50])

normalized = (a - np.min(a)) / (np.max(a) - np.min(a))

print(normalized)