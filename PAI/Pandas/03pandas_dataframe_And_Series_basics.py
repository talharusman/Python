
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
print(newDf.to_numpy())  # Converts the DataFrame to a NumPy array format

# Changing the first cell value back to a float 0.1
newDf.iloc[0, 0] = 0.1

# Sorting the DataFrame:
# If axis=0, it sorts by row index; if axis=1, it sorts by column labels
# Here we're displaying the transposed version of the DataFrame
print(newDf.T.head())

# Sorting the DataFrame based on row index in descending order
print(newDf.sort_index(axis=0, ascending=False).head())

# Demonstrating a copy vs. view scenario in Pandas
newDf2 = newDf  # This creates a reference/pointer; any change in newDf2 will reflect in newDf
CopyDf = newDf[:]  # Alternatively, you can use newDf.copy() to create an independent copy
