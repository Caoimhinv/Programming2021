import numpy as np

A = np.arange(32).reshape(4, 1, 8)
#print(A)

B = np.arange(48).reshape(1, 6, 8)
#print(B)

print(A+B)