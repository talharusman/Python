import pandas as pd

# Load the dataset from the uploaded CSV file
file_path = 'World_Alcoholic_Consumption.csv'
df = pd.read_csv(file_path)

# Filter the data for the years 1987 or 1989
filtered_df = df[(df['Year'] == 1987) | (df['Year'] == 1989)]

# Display the filtered data
print("Alcohol consumption details for the years 1987 or 1989:")
print(filtered_df)
