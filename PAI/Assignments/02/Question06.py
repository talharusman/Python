import numpy as np

matrix = np.array([[4, 7], [2, 6]])
determinant = np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)

print("Matrix:\n", matrix)
print("Determinant:", determinant)
print("Inverse:\n", inverse)
