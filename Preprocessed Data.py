#Preprocessing and cleaning the data for training purposes (will use Pandas for this)
import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

#To lower the size, I will keep those who have rated at least 50 movies, and movies with at least 50 ratings (better representation)
user_counts = ratings['userId'].value_counts()
movie_counts = ratings['movieId'].value_counts()
filtered_ratings = ratings[ratings['userId'].isin(user_counts[user_counts >= 50].index) & ratings['movieId'].isin(movie_counts[movie_counts >= 50].index)]

filtered_ratings.to_csv('cleaned_ratings_full.csv', index = False)
movies.to_csv('cleaned_movies_full.csv', index = False)