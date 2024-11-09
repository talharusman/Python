import numpy as np

array = np.random.rand(25)
percentile_75 = np.percentile(array, 75)
print("Array:", array)
print("75th Percentile:", percentile_75)
