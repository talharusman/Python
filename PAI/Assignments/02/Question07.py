import numpy as np

array = np.random.rand(50)
max_index = np.argmax(array)
min_index = np.argmin(array)

print("Array:", array)
print("Index of Maximum Value:", max_index)
print("Index of Minimum Value:", min_index)
print("Maximum Value:", array[max_index])
print("Minimum Value:", array[min_index])
