import numpy as np
import pandas as pd

dir1 = {
    "name": ['harry', 'rohan', 'talha', 'gaurave'],
    "marks": [78, 24, 99, 10],
    "city": ['KHI', 'HYD', 'SHD', 'ISB']
}

df = pd.DataFrame(dir1)

# Save the DataFrame to a CSV file
df.to_csv('friend.csv')  # Save to 'friend.csv' with default index
df.to_csv('friend_index_false.csv', index=False)  # Save without the index

print(df.head(2))  # Display the first 2 rows
print(df.tail(2))  # Display the last 2 rows
print()
print(df.describe())  # Display statistical summary for numeric columns
#           marks
# count   4.000000
# mean   52.750000
# std    42.547033
# min    10.000000
# 25%    20.500000
# 50%    51.000000
# 75%    83.250000
# max    99.000000
# To avoid the FileNotFoundError, ensure talha.csv exists or create it first
#df.to_csv('talha.csv', index=False)  # This creates the 'talha.csv' file

# Now read the file
talha = pd.read_csv('talha.csv')
print("\nData from talha.csv:")
print(talha)

print(talha['speed'][0])# print the speed at 0 row
talha['speed'][0] = 70#will change the speed
talha.to_csv('talha.csv')
print(talha)
