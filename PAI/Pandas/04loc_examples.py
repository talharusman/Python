
import numpy as np
import pandas as pd


# 'loc' is used for accessing data by label/index. If we had labeled rows or columns,
# we could use 'loc' to access data based on those labels instead of their integer positions.
# For example, if the DataFrame had a column named 'A', we could access it using:
# newDf.loc[0, 'A']


# Creating a DataFrame with 334 rows and 5 columns filled with random float values
newDf = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334))
print(newDf.head(5))  # Display the first 5 rows

# Changing the value of the first cell (row 0, column 0) using 'loc'
newDf.loc[0, 0] = 654  # Access and modify the first row and first column using label-based indexing
print(newDf.head(2))

# Adding a new column labeled '0' with all values set to a default, e.g., 0
newDf[0] = 0  # This creates a new column named '0' with all entries initialized to 0
print(newDf.head(2))

# Changing the column labels to 'A', 'B', 'C', 'D', 'E'
newDf.columns = list("ABCDE")  # Renaming columns back to 'A', 'B', 'C', 'D', 'E'
print(newDf.head(2))

# Adding a new column labeled '0' again after changing column labels
newDf['0'] = 654  # Creates a new column labeled '0' with all entries set to 654
print(newDf.head(2))

# Dropping column '0' using axis=1
newDf = newDf.drop('0', axis=1)  # This will remove column '0'
print(newDf.head(2))

# Demonstrating advanced 'loc' filtering:
# Extracting specific rows and columns using 'loc'
print(newDf.loc[[1, 2], ['C', 'D']])
# This will print rows 1 and 2 for columns 'C' and 'D'

# Using logical conditions with 'loc' to filter data
# It will print all rows where column 'A' is less than 0.4 and column 'C' is greater than 0.1
filtered_data = newDf.loc[(newDf['A'] < 0.4) & (newDf['C'] > 0.1)]
print(filtered_data)
