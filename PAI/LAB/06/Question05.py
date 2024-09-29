import pandas as pd

file_path = 'World_Alcoholic_Consumption.csv'
try:
    df = pd.read_csv(file_path, encoding='utf-8')  # You can change encoding if needed
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty. Please check the content of the CSV file.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the file. Please ensure it's a valid CSV format.")
else:
    # Display the dimensions (shape) of the dataset
    print("Dimensions (Rows x Columns):", df.shape)

    # Extract and display the column names
    print("\nColumn Names:")
    print(df.columns.tolist())
