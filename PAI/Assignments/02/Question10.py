import numpy as np

# Define the normalization function
def normalize(array):
    mean = np.mean(array)
    std_dev = np.std(array)
    normalized_array = (array - mean) / std_dev
    return normalized_array

sample_array = np.array([10, 20, 30, 40, 50])

normalized_sample = normalize(sample_array)
print("Original Array:", sample_array)
print("Normalized Array:", normalized_sample)
