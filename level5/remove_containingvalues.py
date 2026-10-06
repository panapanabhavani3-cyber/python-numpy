import numpy as np

a = np.array([[1, 2, 3],
              [4, np.nan, 6],
              [7, 8, 9],
              [np.nan, 11, 12]])

result = a[~np.isnan(a).any(axis=1)]

print(result)