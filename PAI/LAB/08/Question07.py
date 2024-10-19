
import numpy as np

random_array = np.random.rand(1000)

average = np.mean(random_array)
variance = np.var(random_array)
std_deviation = np.std(random_array)

filename = "stats_file.txt"
with open(filename, 'w') as file:
    file.write(f"Average: {average}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard Deviation: {std_deviation}\n")

print(f"Results saved to {filename}")
