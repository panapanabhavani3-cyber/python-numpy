import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

transpose = a.T

print(transpose)
print("Original shape:", a.shape)
print("Transpose shape:", transpose.shape)