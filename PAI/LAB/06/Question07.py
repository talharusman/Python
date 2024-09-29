import pandas as pd

file_path = 'employee.xlsx'

try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")
else:
    print("First few rows of the dataset:")
    print(df.head())

    specified_year = 2022

    filtered_employees = df[df['Joining_Year'] == specified_year]

    print(f"\nList of employees who joined in the year {specified_year}:")
    print(filtered_employees)
