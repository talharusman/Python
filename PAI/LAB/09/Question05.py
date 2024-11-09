import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Education_2.csv')

# Count the number of males and females
M_couny = df[df['Gender'] == 'Male'].shape[0]
F_count = df[df['Gender'] == 'Female'].shape[0]

# Prepare data for plotting
counts = [M_couny, F_count]
labels = ['Male', 'Female']

# Create the pie chart
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'pink'], shadow=False)
plt.title('Gender Distribution Among Students')
plt.show()