import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('seaLevel.csv')

a = df[df['year'] > 1924]

x = a['year']
y = a['mmfrom1993-2008average']

plt.scatter(x, y, color='green')
plt.title('Sea Level Over Time (Post-1924)')
plt.show()