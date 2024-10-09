import pandas as pd

df = pd.read_csv("heart.csv")
new_df = df[(df["cp"] == 2)]
print(new_df)
