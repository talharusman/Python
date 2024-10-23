from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("new.csv")
x = df["Species"]
y = df["PetalWidthCm"]
color = ['green', 'purple', 'yellow', 'blue','red']
plt.scatter(x, y, c=color , marker="*")

plt.show()