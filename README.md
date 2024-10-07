# Movie-Recommender-with-Some-Visualisation

This project is a **Movie Recommendation System** with integrated data visualizations to provide insights into the dataset. The application uses collaborative filtering and genre similarity matrices to recommend movies based on user inputs. Below is a detailed overview of the data visualizations, insights, and the machine learning models implemented.

## Project Overview
The main aim of this project is to create a movie recommendation system using collaborative filtering and genre similarity. Additionally, it includes various data visualizations to better understand user preferences and movie ratings.

## Visualizations & Insights

### 1. Distribution of Movie Ratings
![Distribution of Movie Ratings](images/Distribution_of_Movie_Ratings.png)

**Insight**:  
The distribution shows how users perceive movies overall. Higher peaks around higher ratings suggest that most users rate movies favorably, indicating a general satisfaction with movie quality.

### 2. Top 10 Movies by Rating Count
![Top 10 Movies by Rating Count](images/Top_10_Movies_by_Rating_Count.png)

**Insight**:  
The top movies by rating count indicate the most popular movies that have a large number of users rating them. This shows which movies have widespread appeal and a large viewer base.

### 3. Genre Distribution of Movies
![Genre Distribution of Movies](images/Genre_Distribution_of_Movies.png)

**Insight**:  
This pie chart shows the distribution of genres among movies. Certain genres like Drama and Comedy dominate the distribution, indicating their popularity and frequency in the dataset. Lesser-known genres like Film-Noir and IMAX are niche genres with fewer entries.

### 4. Average Ratings by Genre
![Average Ratings by Genre](images/Average_Ratings_by_Genre.png)

**Insight**:  
This bar plot highlights the average ratings for each genre, showing which genres are generally rated higher by the audience. Genres like Film-Noir, War, and Documentary tend to receive higher average ratings, while genres like Horror and Comedy receive lower ratings.

## Machine Learning Models Used

### Collaborative Filtering (Model 1)
- **Description**:  
  Collaborative filtering is used to recommend movies based on user-item interactions. This model predicts ratings by taking into account similar users' preferences.
  
- **Algorithm**:  
  The implementation uses the **Singular Value Decomposition (SVD)** algorithm from the Surprise library to predict movie ratings.
  
- **Output**:  
  The collaborative filtering model outputs a list of movies that are most likely to be of interest to the user based on their past preferences.

### Genre Similarity Matrix (Model 2)
- **Description**:  
  The genre similarity matrix model recommends movies based on similarity in genre features. This is useful for users who are looking for similar movies to a particular one they enjoyed.
  
- **Implementation**:  
  The model uses a cosine similarity matrix calculated based on the genre features of each movie.
  
- **Output**:  
  A list of movies that are most similar in genre to the selected movie.

## How to Use the Movie Recommender System

### Interface Overview
1. **Search for a Movie**:
   - Enter a movie title or Movie ID to look up movies in the dataset.
   - Choose the movie from the results to get started.

2. **Choose Recommendation Method**:
   - **Collaborative Filtering**: Recommends movies based on user ratings.
   - **Genre Similarity Matrix**: Recommends movies similar in genre to the selected one.

3. **View Recommendations**:
   - See a list of recommended movies based on the selected method.
   - Each recommendation is accompanied by its title and ID for reference.

## Project Structure
- `images/`: Contains all images used in this README for visualizations.
- `Model 1 (CF).py`: Script for Collaborative Filtering Model.
- `Model 2 (GSM).py`: Script for Genre Similarity Model.
- `Preprocessed Data.py`: Script for cleaning and processing the raw data.
- `datavis.py`: Script for generating visualizations and insights.
- `maincode.py`: The main script for the movie recommendation system.
- `README.md`: Project documentation file.
- `index.html`: A simple portfolio site showcasing the project.

## How to Run the Project Locally
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/kareemcodes-2000/Movie-Recommender-with-Some-Visualisation.git
