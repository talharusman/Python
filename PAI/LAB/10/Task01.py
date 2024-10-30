import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('heart.csv')

plt.figure(figsize=(10, 8))

plt.subplot(4, 4, 1)
plt.hist(df['age'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.title('Age')

plt.subplot(4, 4, 2)
plt.hist(df['sex'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Sex')
plt.title('Sex')

plt.subplot(4, 4, 3)
plt.hist(df['cp'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('CP')

plt.subplot(4, 4, 4)
plt.hist(df['trestbps'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('value')
plt.title('Trestbps')

plt.subplot(4, 4, 5)
plt.hist(df['chol'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('CHOL')

plt.subplot(4, 4, 6)
plt.hist(df['fbs'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('FBS')

plt.subplot(4, 4, 7)
plt.hist(df['restecg'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Restecg')

plt.subplot(4, 4, 8)
plt.hist(df['thalach'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Thalach')

plt.subplot(4, 4, 9)
plt.hist(df['exang'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Exang')

plt.subplot(4, 4, 10)
plt.hist(df['oldpeak'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Oldpeak')

plt.subplot(4, 4, 11)
plt.hist(df['slope'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Slope')

plt.subplot(4, 4, 12)
plt.hist(df['ca'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('CA')

plt.subplot(4, 4, 13)
plt.hist(df['thal'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Thal')

plt.subplot(4, 4, 14)
plt.hist(df['target'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.title('Target')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 10))  # Increase the figure size
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.show()

plt.figure(figsize=(8, 6))

plt.pie(df['sex'].value_counts() ,labels=['Male', 'Female'], autopct="%1.1f%%")
plt.show()

sns.displot(df,x='chol',kde=True)
sns.displot(df,x='thalach',kde=True)
sns.displot(df,x='age',kde=True)
sns.displot(df,x='trestbps',kde=True)
plt.show()