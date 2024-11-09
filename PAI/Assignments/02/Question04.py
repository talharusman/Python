import numpy as np

# Define two NumPy arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Element-wise operations using NumPy functions
addition = np.add(array1, array2)
subtraction = np.subtract(array1, array2)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)

# Display the results
print("Array 1:", array1)
print("Array 2:", array2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
