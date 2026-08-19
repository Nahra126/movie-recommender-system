import pickle
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
vectors = pickle.load(open('vectors.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Similarity ab yahan calculate hogi, sirf is movie ke liye
    distances = cosine_similarity(vectors[movie_index], vectors)[0]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('🎬 Movie Recommendation System')

selected_movie = st.selectbox(
    'Apni pasandeeda movie select karein:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader('Aapko ye movies bhi pasand aa sakti hain:')
    for movie in recommendations:
        st.write(movie)