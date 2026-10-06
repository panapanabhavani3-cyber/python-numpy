import numpy as np

a = np.array([10, 20, 30, 40, 50])

mean = np.mean(a)
result = a[a > mean]

print("Mean:", mean)
print("Values above mean:", result)