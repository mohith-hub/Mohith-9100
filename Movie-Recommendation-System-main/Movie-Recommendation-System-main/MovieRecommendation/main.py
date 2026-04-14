import streamlit as st
import pandas as pd
import pickle

# Load your pre-trained model and movie data
# Make sure you have these files saved earlier
movies = pd.read_pickle('movies.pkl')  # DataFrame with at least 'title' column
similarity = pd.read_pickle('similarity.pkl')  # similarity matrix

# Function to get recommendations
def recommend(movie_name):
    movie_name = movie_name.lower()
    if movie_name not in movies['title'].str.lower().values:
        return "Movie not found. Please check spelling."
    
    idx = movies[movies['title'].str.lower() == movie_name].index[0]
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]  # top 5
    recommended_movies = [movies.iloc[i[0]]['title'] for i in distances]
    return recommended_movies

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Type your favorite movie and get recommendations!")

# Movie input
movie_input = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    recommendations = recommend(movie_input)
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.success("We recommend:")
        for i, movie in enumerate(recommendations, start=1):
            st.write(f"{i}. {movie}")
