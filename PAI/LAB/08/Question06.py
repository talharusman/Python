import numpy as np

arr1 = np.arange(1, 16)
a = arr1.reshape(5, 3)

arr2 = np.arange(1, 7)
b = arr2.reshape(3, 2)

c = np.matmul(a, b)  # or c = a @ b

print(a, '\n')
print(b, '\n')
print(c, '\n')