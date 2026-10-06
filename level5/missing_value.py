import numpy as np

a = np.array([10, 20, np.nan, 40, np.nan, 60])

missing = np.isnan(a).sum()
percentage = (missing / a.size) * 100

print("Missing values:", missing)
print("Missing percentage:", percentage, "%")