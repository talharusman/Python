import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('education_1.csv')

l1 = ['1 - 14', '15 - 30']

a = df[(df['Student Age'] > 10) & (df['Student Age'] <= 15)].shape[0]
b = df[(df['Student Age'] > 15) & (df['Student Age'] <= 30)].shape[0]

l2 = [a,b]
plt.pie(l2,labels=l1)
plt.show()