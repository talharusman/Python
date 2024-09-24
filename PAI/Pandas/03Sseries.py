from operator import index

import numpy as np
import numpy.random
import pandas as pd

# Creating a Pandas Series with 30 random float values
ser = pd.Series(np.random.rand(30))
print(ser)
print(type(ser))

# Creating a DataFrame with 334 rows and 5 columns filled with random float values
newDf = pd.DataFrame(numpy.random.rand(334, 5), index=np.arange(334))
print(newDf.head(5))  # Display the first 5 rows
print(type(newDf))

# Displaying the data types of each column in the DataFrame
print(newDf.dtypes)

# Changing the value of the first cell (row 0, column 0) to the string 'talha'
newDf.iloc[0, 0] = 'talha'  # Used iloc for integer-based indexing
print(newDf.head())

# Displaying the data types again to see the changes (now column 0 will be of object type due to mixed types)
print(newDf.dtypes)

# Printing the index range of the DataFrame
print(newDf.index)

# Printing the column labels of the DataFrame
print(newDf.columns)

# Converting the DataFrame to a NumPy array

 # Converts the DataFrame to a NumPy array format
print(newDf.to_numpy() )

# Changing the first cell value back to a float 0.1
newDf.iloc[0, 0] = 0.1

# Sorting the DataFrame:
# If axis=0, it sorts by row index; if axis=1, it sorts by column labels
# Here we're displaying the transposed version of the DataFrame
print(newDf.T.head())

# Sorting the DataFrame based on row index in descending order
print(newDf.sort_index(axis=0, ascending=False).head())

# newDf2 is a view/reference to newDf; changes in newDf2 will also affect newDf
newDf2 = newDf  # This creates a reference/pointer; any change in newDf2 will reflect in newDf

# CopyDf is an independent copy of newDf; changes in CopyDf will NOT affect newDf
CopyDf = newDf[:]  # Alternatively, you can use newDf.copy()

# Demonstrating the use of 'loc':
# 'loc' allows access and modification by label-based indexing
# Here, we are changing the value in the first row and first column to 654
newDf.loc[0, 0] = 654
print(newDf.head(2))

# Adding a new column labeled '0' with all values set to a default, e.g., 0
newDf[0] = 0  # This creates a new column named '0' with all entries initialized to 0
print(newDf.head(2))

# Changing the column labels to 'A', 'B', 'C', 'D', 'E' again
newDf.columns = list("ABCDE")  # Renaming columns back to 'A', 'B', 'C', 'D', 'E'
print(newDf.head(2))

# Adding a new column labeled '0' again after changing column labels
newDf['0'] = 654  # Creates a new column labeled '0' with all entries set to 654
print(newDf.head(2))

# Dropping column 'A' using axis=1
newDf = newDf.drop('0', axis=1)  # This will remove column 'A'
print(newDf.head(2))

print(newDf.loc[[1,2], ['C','D']])
# it only will print the 1 and 2 for and c,d colum
# if in this we use colon(:) int the place of 1,2  it prints all the row and wisewersa

print(newDf.loc[newDf['A'] < 0.4] & (newDf['C'] > 0.1))
# it will print all the data of column a which has value is lass then 0.4, and
# column C is greater then 0.1