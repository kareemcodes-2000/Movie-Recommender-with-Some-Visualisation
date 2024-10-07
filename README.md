# Movie-Recommender-with-Some-Visualisation

This project is a **Movie Recommendation System** with integrated data visualizations to provide insights into the dataset. The application uses collaborative filtering and genre similarity matrices to recommend movies based on user inputs. Below is a detailed overview of the data visualizations, insights, and the machine learning models implemented.

## Project Overview
The main aim of this project is to create a movie recommendation system using collaborative filtering and genre similarity. Additionally, it includes various data visualizations to better understand user preferences and movie ratings.

## Visualizations & Insights

### 1. Distribution of Movie Ratings
![Distribution of Movie Ratings](images/Distribution%20of%20Movie%20Ratings.PNG)

**Insight:**  
The distribution shows how users perceive movies overall. Higher peaks around higher ratings suggest that most users rate movies favorably, indicating a general satisfaction with movie quality.

---

### 2. Top 10 Movies by Rating Count
![Top 10 Movies by Rating Count](images/Top%2010%20Movies%20By%20Rating%20Count.PNG)

**Insight:**  
The top movies by rating count indicate the most popular movies that have a large number of users rating them. This shows which movies have widespread appeal and a large viewer base.

---

### 3. Genre Distribution of Movies
![Genre Distribution of Movies](images/Genre%20Distribution%20of%20Movies.PNG)

**Insight:**  
This table shows the distribution of genres among movies. Certain genres like Drama and Comedy dominate the distribution, indicating their popularity and frequency in the dataset. Lesser-known genres like Film-Noir and IMAX are niche genres with fewer entries.

---

### 4. Genre Distribution of Movies (Pie Chart)
![Genre Distribution of Movies Pie Chart](images/Genre%20Distribution%20of%20Movies%20Pie%20Chart.PNG)

**Insight:**  
This pie chart visualizes the percentage distribution of genres. Certain genres dominate the distribution, while others are less common.

---

### 5. Average Ratings by Genre
![Average Ratings Per Genre](images/Average%20Ratings%20Per%20Genre.PNG)

**Insight:**  
This bar plot highlights the average ratings for each genre, showing which genres are generally rated higher by the audience. Genres like Film-Noir, War, and Documentary tend to receive higher average ratings, while genres like Horror and Comedy receive lower ratings.

---

## Machine Learning Models Used

### **Collaborative Filtering (Model 1)**  
**Description:**  
Collaborative filtering is used to recommend movies based on user-item interactions. This model predicts ratings by taking into account similar users' preferences.

**Algorithm:**  
The implementation uses the Singular Value Decomposition (SVD) algorithm from the Surprise library to predict movie ratings.

**Output:**  
The collaborative filtering model outputs a list of movies that are most likely to be of interest to the user based on their past preferences.

---

### **Genre Similarity Matrix (Model 2)**  
**Description:**  
The Genre Similarity Matrix is based on the genres associated with each movie. This model computes the similarity between different movies based on their genre metadata.

**Algorithm:**  
A similarity matrix is generated using cosine similarity, and the closest matching movies are recommended based on the genre structure.

**Output:**  
The genre similarity model outputs a list of movies that are similar to the selected movie based on genre composition.
