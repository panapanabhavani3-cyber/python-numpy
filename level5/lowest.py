import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

column_avg = np.mean(a, axis=0)
column = np.argmin(column_avg)

print("Column with lowest average:", column)
print("Lowest average:", column_avg[column])