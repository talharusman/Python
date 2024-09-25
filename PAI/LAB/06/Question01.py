import pandas as pd
movies_data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'revenue': [3000000, 1500000, 2500000, 500000, 1000000],
    'budget': [800000, 1200000, 900000, 400000, 700000]
}
df = pd.DataFrame(movies_data)
filtered_movies = df[(df['revenue'] > 2000000) & (df['budget'] < 1000000)]

# filtered_movies_dict = filtered_movies.to_dict(orient='records')


# print("Movies with revenue more than 2 million and budget less than 1 million:")
# for movie in filtered_movies_dict:
#     print(movie)
print(filtered_movies)
