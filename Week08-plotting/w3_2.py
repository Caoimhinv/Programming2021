import numpy as np

table = np.array([
    [5, 3, 7, 1],
    [2, 6, 7 ,9],
    [1, 1, 1, 1],
    [4, 3, 2, 0],
])
# prints hisgest value in entire array (default)
print(table.max())
# prints highest value for each column and returns a 1D array
print(table.max(axis=0))
# prints highest value for each row and returns a 1D array
print(table.max(axis=1))

