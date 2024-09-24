import numpy as np
import pandas as pd

# Creating a DataFrame with 334 rows and 5 columns filled with random float values
newDf = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334))

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(newDf.head(5))

# Assigning column names to the DataFrame
newDf.columns = list("ABCDE")
print("\nDataFrame after assigning column names:")
print(newDf.head(5))

# Printing the value in the first row (row 0) and the last column (column 4)
print("\nValue in the first row (row 0) and the last column (column 'E'):")
print(newDf.iloc[0, 4])  # 'iloc' is used to access data by position (row and column number)

# 'loc' is used for accessing data by label/index. If we had labeled rows or columns,
# we could use 'loc' to access data based on those labels instead of their integer positions.
# For example, if the DataFrame had a column named 'A', we could access it using:
# newDf.loc[0, 'A']

# Dropping the first row (row 0) and displaying the first 3 rows of the modified DataFrame
print("\nDataFrame after dropping the first row (row 0):")
print(newDf.drop(0).head(3))  # This returns a copy of newDf without the first row

# Corrected drop method to remove specific columns
# Dropping columns 'A' and 'C' in place (modifying the original DataFrame)
newDf.drop(columns=['A', 'C'], inplace=True)

# Displaying the first 3 rows after dropping columns 'A' and 'C'
print("\nDataFrame after dropping columns 'A' and 'C':")
print(newDf.head(3))

newDf.drop(index=[0], inplace=True)
print("\nDataFrame after dropping index 0:")
print(newDf.head(3))

newDf.reset_index(drop= True,inplace=True)
print("After reset of index: ")
print(newDf.head(3))

print(newDf['B'].isnull())# it will return the truth value where is B column is null

newDf.loc[:, ['B']] = None
print(newDf['B'].isnull())# it will return the truth value where is B column is null



