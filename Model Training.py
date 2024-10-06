#I want to try two types of machine learning in this (abit ambitious I know, but it's for learning!)
#We will use collaborative filtering and genre similarity matrix, and save it to joblib.

import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import joblib

ratings = pd.read_csv('cleaned_ratings_full.csv')
movies = pd.read_csv('cleaned_movies_full.csv')

#Section 1: Collaborative Filtering Model using SVD
reader = Reader(rating_scale=(0.5,5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)

svd_model = SVD()
svd_model.fit(trainset)
joblib.dump(svd_model, 'svd_model_full.pk1')

#Section 2: Build a genre similarity matrix
movies['genres'] = movies['genres'].fillna('')
genre_data = movies['genres'].str.get_dummies('|')
genre_similarity = pd.DataFrame(cosine_similarity(genre_data), index = movies['movieId'], columns = movies['movieId']
joblib.dump(genre_similarity, 'genre_similarity_matrix.pk1')