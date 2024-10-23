from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")
x = df["Species"]
y = df["SepalLengthCm"]
clr = ['g', 'm', 'y', 'b']
plt.bar(x, y, color=clr)
plt.show()