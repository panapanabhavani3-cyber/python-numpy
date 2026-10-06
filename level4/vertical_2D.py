import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

result = np.hsplit(a, 2)

print(result[0])
print(result[1])