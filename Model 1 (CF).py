import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import joblib

ratings = pd.read_csv('cleaned_ratings_full.csv')
movies = pd.read_csv('cleaned_movies_full.csv')

#Section 1: Collaborative Filtering Model using SVD
print("Training collaborative filtering model (SVD)...")
reader = Reader(rating_scale=(0.5,5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)

svd_model = SVD()
svd_model.fit(trainset)
joblib.dump(svd_model, 'svd_model_full.pk1')
print("Collaborative filtering model saved as 'svd_model_full.pkl'.")