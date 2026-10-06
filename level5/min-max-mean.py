import numpy as np

a = np.random.randint(1, 101, size=(10, 10))

print("Matrix:")
print(a)

print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))