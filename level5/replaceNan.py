import numpy as np

a = np.array([10, 20, np.nan, 40, np.nan, 60])

mean = np.nanmean(a)
a[np.isnan(a)] = mean

print(a)