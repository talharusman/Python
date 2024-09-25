import pandas as pd
import numpy as np

movies_data = {
    'title': ['Inception', 'The Matrix', 'Interstellar', 'Parasite', 'The Godfather'],
    'runtime': [148, 136, 169, 132, 175],   # Runtime in minutes
    'revenue': [829895144, 463517383, 677471339, 258660000, 245066411],  # Revenue in dollars
    'budget': [160000000, 63000000, 165000000, 11400000, 6000000]        # Budget in dollars
}

df =  pd.DataFrame(movies_data)
sorted= df.sort_values(by='runtime', ascending=False)

print(sorted)
