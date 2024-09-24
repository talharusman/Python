import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column
df['Salary'] = [70000, 80000, 90000]

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# Filter the DataFrame for people older than 28
filtered_df = df[df['Age'] > 28]

# Display the filtered DataFrame
print("\nFiltered DataFrame (Age > 28):")
print(filtered_df)

# Calculate the average salary
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: ${average_salary:.2f}")
