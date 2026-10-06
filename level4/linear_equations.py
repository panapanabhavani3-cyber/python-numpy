import numpy as np

a = np.array([[2, 1],
              [1, 3]])

b = np.array([5, 6])

result = np.linalg.solve(a, b)

print(result)