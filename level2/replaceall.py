import numpy as np

arr = np.array([50, 120, 80, 150, 90])

arr[arr > 100] = 100

print(arr)