import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache_data
def load_data():
    movies = pd.read_csv('cleaned_movies_full.csv')
    ratings = pd.read_csv('cleaned_ratings_full.csv')
    return movies, ratings

# Define visualization and analysis functions
def visualize_movie_data(movies, ratings):
    # Title
    st.title("Movie Data Visualizations and Insights")

    # Data Sample Section
    st.subheader("Data Samples for Debugging:")
    st.write("Movies Data Sample:")
    st.dataframe(movies.head())  # Show first few rows of movies data
    st.write("Ratings Data Sample:")
    st.dataframe(ratings.head())  # Show first few rows of ratings data

    # Column Statistics
    st.write("Rating Column Summary:")
    st.table(ratings['rating'].describe())

    # Visualization 1: Distribution of Movie Ratings
    st.subheader("Visualization 1: Distribution of Movie Ratings")
    plt.figure(figsize=(10, 6))
    sns.histplot(ratings['rating'], bins=10, kde=True, color='skyblue')
    plt.title("Distribution of Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    st.pyplot(plt)
    st.markdown(
        "**Insight**: The distribution shows how users perceive movies overall. Higher peaks around higher ratings suggest that most users rate movies favorably."
    )

    # Visualization 2: Top 10 Movies by Rating Count
    st.subheader("Visualization 2: Top 10 Movies by Rating Count")
    top_movies = ratings['movieId'].value_counts().head(10).index
    top_movie_counts = ratings['movieId'].value_counts().head(10)
    top_movie_titles = movies[movies['movieId'].isin(top_movies)][['movieId', 'title']].set_index('movieId')
    top_movie_titles['Rating Count'] = top_movie_counts.values
    st.table(top_movie_titles)

    # Barplot for Top Movies
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Rating Count', y='title', data=top_movie_titles.reset_index(), palette='viridis')
    plt.title("Top 10 Movies by Rating Count")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Movie Title")
    st.pyplot(plt)
    st.markdown(
        "**Insight**: The top movies by rating count indicate the most popular movies that have a large number of users rating them."
    )

    # Visualization 3: Genre Distribution of Movies
    st.subheader("Visualization 3: Genre Distribution of Movies")
    all_genres = movies['genres'].str.split('|').explode().value_counts()
    genre_df = pd.DataFrame({'Genre': all_genres.index, 'Count': all_genres.values})
    st.table(genre_df)

    # Pie Chart for Genre Distribution
    plt.figure(figsize=(10, 10))
    plt.pie(genre_df['Count'], labels=genre_df['Genre'], autopct='%1.1f%%', startangle=140)
    plt.title("Genre Distribution of Movies")
    st.pyplot(plt)
    st.markdown(
        "**Insight**: This pie chart shows the distribution of genres among movies. Certain genres dominate the distribution, indicating their popularity and frequency in the dataset."
    )

    # Visualization 4: Average Ratings by Genre
    st.subheader("Visualization 4: Average Ratings by Genre")
    genre_ratings = ratings.merge(movies[['movieId', 'genres']], on='movieId')
    genre_ratings['genres'] = genre_ratings['genres'].str.split('|')
    genre_exploded = genre_ratings.explode('genres')

    avg_genre_ratings = genre_exploded.groupby('genres')['rating'].mean().reset_index()
    avg_genre_ratings.columns = ['Genre', 'Average Rating']
    st.table(avg_genre_ratings)

    # Barplot for Average Ratings by Genre
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Average Rating', y='Genre', data=avg_genre_ratings.sort_values(by='Average Rating', ascending=False), palette='coolwarm')
    plt.title("Average Ratings by Genre")
    plt.xlabel("Average Rating")
    plt.ylabel("Genre")
    st.pyplot(plt)
    st.markdown(
        "**Insight**: This bar plot highlights the average ratings for each genre, showing which genres are generally rated higher by the audience."
    )

# Main Function
def main():
    # Load the data
    movies, ratings = load_data()
    
    # Call visualization function
    visualize_movie_data(movies, ratings)

# Run the Streamlit App
if __name__ == '__main__':
    main()
