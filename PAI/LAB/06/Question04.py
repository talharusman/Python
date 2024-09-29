import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Talha', 'Saif', 'Abdul Rahman'],
    'Age': [20, 20, 21],
    'City': ['SHD', 'KHI', 'KHI']
}

df = pd.DataFrame(data)

df.index = pd.RangeIndex(start=100, stop=100 + len(df), step=1)

print(df)
