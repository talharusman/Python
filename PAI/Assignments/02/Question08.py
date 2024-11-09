import numpy as np

A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 5, 3]])
B = np.array([1, 2, 3])
solution = np.linalg.solve(A, B)

print("Solution for [x, y, z]:", solution)
