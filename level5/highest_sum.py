import numpy as np

a = np.array([[1, 2, 3],
              [10, 20, 30],
              [4, 5, 6]])

row_sums = np.sum(a, axis=1)
row = np.argmax(row_sums)

print("Row with highest sum:", row)
print("Highest sum:", row_sums[row])