# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Choose number of movies to use
top_n_movies = 300000

# Step 1: Load the movie dataset
print("Loading movie data...")
movies = pd.read_csv('cleaned_movies_full.csv')  
ratings = pd.read_csv('cleaned_ratings_full.csv') 

# Step 2: Filter for the top 'n' most rated movies
print(f"Selecting the top {top_n_movies} most rated movies...")
movie_rating_counts = ratings['movieId'].value_counts()
top_movies = movie_rating_counts.head(top_n_movies).index

# Filter the movies and ratings data
filtered_movies = movies[movies['movieId'].isin(top_movies)]
filtered_ratings = ratings[ratings['movieId'].isin(top_movies)]

# Step 3: Preprocess genres data for similarity calculation
print("Preprocessing genre data...")
filtered_movies['genres'] = filtered_movies['genres'].fillna('')

# Create a one-hot encoded genre matrix
genre_data = filtered_movies['genres'].str.get_dummies('|')

# Step 4: Calculate the Genre Similarity Matrix
print("Calculating genre similarity matrix...")
# Use cosine similarity to compute genre similarity between movies
genre_similarity = pd.DataFrame(
    cosine_similarity(genre_data), 
    index=filtered_movies['movieId'], 
    columns=filtered_movies['movieId']
)

# Step 5: Save the Genre Similarity Matrix
print(f"Saving genre similarity matrix for top {top_n_movies} movies...")
joblib.dump(genre_similarity, f'genre_similarity_matrix_top_{top_n_movies}.pkl')  # Save matrix to a .pkl file

print("Genre similarity matrix successfully created and saved!")