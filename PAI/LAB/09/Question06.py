import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Names': ['Raghib', 'Fahad', 'Abdul Rahman', 'Umar', 'Talha', 'Saif', 'Adina', 'Sara', 'Hafsa', 'Arwa'],
    'Science': [50, 80, 40, 50, 40, 85, 84, 95, 95, 85],
    'Maths': [100, 58, 85, 48, 58, 75, 82, 99, 85, 95]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Optional: Set figure size for better visibility
plt.scatter(df['Names'], df['Science'], color='blue', label='Science')
plt.scatter(df['Names'], df['Maths'], color='pink', label='Maths')

# Set labels and title
plt.xlabel('Student Names')
plt.ylabel('Scores')
plt.title('Scores in Science and Maths')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()

# Show the plot
plt.tight_layout()  # Optional: Adjust layout to prevent clipping of tick-labels
plt.show()