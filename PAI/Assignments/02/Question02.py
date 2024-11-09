import numpy as np

# Generate a 3x3 matrix with random integers between 1 and 10
matrix = np.random.randint(1, 11, size=(3, 3))

transpose_matrix = matrix.T

print("Original Matrix:\n", matrix)
print("Transpose of the Matrix:\n", transpose_matrix)
