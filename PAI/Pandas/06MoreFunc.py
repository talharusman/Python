import pandas as pd
import numpy as np


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, np.nan, np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})

print(df.head())
print(df.dropna(how = 'all', axis=1))