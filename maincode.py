import pandas as pd
import streamlit as st
import joblib
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

# Load Data In
@st.cache_data
def load_data():
    # Load movies and ratings
    movies = pd.read_csv('cleaned_movies_full.csv')
    ratings = pd.read_csv('cleaned_ratings_full.csv')
    return movies, ratings

# Load models and similarity matrix
@st.cache_resource
def load_models():
    # Load pre-trained models and similarity matrices
    svd_model = joblib.load('svd_model_full.pk1')  # collaborative model
    genre_similarity_matrix = joblib.load('genre_similarity_matrix_top_300000.pkl')  # genre similarity matrix model
    return svd_model, genre_similarity_matrix

# Sidebar for movie search
def search_movie_sidebar(movies):
    st.sidebar.title("User Options")
    st.sidebar.header("Search for Movie")

    # Option to search by Movie ID or Movie Title
    search_option = st.sidebar.radio("Search by:", ('Movie Title', 'Movie ID'))

    # Input field based on the search type
    if search_option == 'Movie Title':
        movie_title = st.sidebar.text_input("Enter Movie Title")
        movie_id = None
        if movie_title:
            # Find the movie ID by title
            result = movies[movies['title'].str.contains(movie_title, case=False, na=False)]
            st.sidebar.write(result[['movieId', 'title']].reset_index(drop=True))
            if not result.empty:
                movie_id = st.sidebar.number_input("Choose a Movie ID", min_value=int(result['movieId'].min()),
                                                   max_value=int(result['movieId'].max()), step=1)
    else:
        # Input for Movie ID
        movie_id = st.sidebar.number_input("Enter Movie ID", min_value=1, step=1)

    return movie_id

# Recommendation functions
def get_recommendations_collaborative(movie_id, ratings, svd_model, movies, top_n=10):
    # Check if the movie has enough ratings
    if movie_id not in ratings['movieId'].values:
        return ["Movie not found or insufficient data for collaborative filtering"]

    # Use the pre-trained SVD model for predictions
    user_id = 99999  # Placeholder virtual user ID for generating recommendations
    pred_ratings = []

    # Generate predictions for all movie IDs
    for mid in ratings['movieId'].unique():
        pred_ratings.append((mid, svd_model.predict(user_id, mid).est))  # Using the pre-trained model

    # Sort by predicted rating
    sorted_movies = sorted(pred_ratings, key=lambda x: x[1], reverse=True)

    # Select top N recommendations excluding the current movie
    top_recommendations = [item[0] for item in sorted_movies if item[0] != movie_id][:top_n]

    # Map movie IDs to titles and format the output
    filtered_titles = movies[movies['movieId'].isin(top_recommendations)]
    return filtered_titles[['movieId', 'title']].apply(lambda row: f"{row['title']} (ID: {row['movieId']})", axis=1).tolist()


def get_recommendations_genre(movie_id, movies, genre_similarity_matrix, top_n=10):
    # Check if the movie ID exists in the genre similarity matrix
    if movie_id in genre_similarity_matrix.index:

        # Use pre-existing similarity matrix
        similar_movies = genre_similarity_matrix[movie_id].sort_values(ascending=False).head(top_n + 1).index[1:]
        
        similar_movies = [mid for mid in similar_movies]

        # Filter for titles
        filtered_titles = movies[movies['movieId'].isin(similar_movies)]

        # Convert to a list of formatted strings for better display
        return filtered_titles[['movieId', 'title']].apply(lambda row: f"{row['title']} (ID: {row['movieId']})", axis=1).tolist()
    else:
        st.write("Movie not found in pre-generated genre similarity matrix.")
        return ["Movie not found in pre-generated genre similarity matrix"]

# Streamlit application layout
def main():
    st.title("Movie Recommendation System")

    # Load data
    movies, ratings = load_data()
    svd_model, genre_similarity_matrix = load_models()

    # Sidebar for movie lookup
    movie_id = search_movie_sidebar(movies)

    # Final input ID (selected movie)
    st.sidebar.subheader("Final Input ID")
    final_movie_id = st.sidebar.number_input("Input Movie ID for Recommendation", min_value=1, value=int(movie_id or 1))

    # Select recommendation method
    recommendation_method = st.sidebar.selectbox("Select Recommendation Method",
                                                 ["Use Collaborative Filtering", "Use Genre Similarity Matrix"])

    if st.sidebar.button('Get Recommendations'):
        st.write(f'Generating recommendations for Movie ID: {final_movie_id}...')

        # Recommendation generation logic
        if recommendation_method == 'Use Collaborative Filtering':
            st.subheader('Collaborative Filtering Recommendations')
            recommendations = get_recommendations_collaborative(final_movie_id, ratings, svd_model, movies)
            
        else:
            st.subheader('Genre Similarity Matrix Recommendations')
            recommendations = get_recommendations_genre(final_movie_id, movies, genre_similarity_matrix)
        
        # Display recommendations
        if isinstance(recommendations, list) and len(recommendations) > 0:
            for rec in recommendations:
                st.write(f"**{rec}**")
        else:
            st.write('No recommendations found')

# Run the app
if __name__ == '__main__':
    main()
