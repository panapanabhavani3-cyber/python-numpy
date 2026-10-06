import numpy as np

arr = np.array([-10, 20, -30, 40, -50])

arr[arr < 0] = 0

print(arr)