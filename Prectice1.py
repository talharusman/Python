from matplotlib import pyplot as plt
import  pandas as pd

df=pd.read_csv("Iris.csv")
x=df["Id"]
y=df["SepalLengthCm"]
plt.plot(x,y)
plt.show()