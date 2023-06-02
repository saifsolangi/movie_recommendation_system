import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('./model_files/movies.pkl','rb'))
similarity = pickle.load(open('./model_files/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    c1,c2,c3,c4,c5= st.columns(5)
    c6,c7,c8,c9,c10= st.columns(5)
    
    with st.container():
        c1.write(recommended_movie_names[0])
        c1.image(recommended_movie_posters[0])
        c2.write(recommended_movie_names[1])
        c2.image(recommended_movie_posters[1])
        c3.write(recommended_movie_names[2])
        c3.image(recommended_movie_posters[2])
        c4.write(recommended_movie_names[3])
        c4.image(recommended_movie_posters[3])
        c5.write(recommended_movie_names[4])
        c5.image(recommended_movie_posters[4])
    with st.container():
        c6.write(recommended_movie_names[5])
        c6.image(recommended_movie_posters[5])
        c7.write(recommended_movie_names[6])
        c7.image(recommended_movie_posters[6])
        c8.write(recommended_movie_names[7])
        c8.image(recommended_movie_posters[7])
        c9.write(recommended_movie_names[8])
        c9.image(recommended_movie_posters[8])
        c10.write(recommended_movie_names[9])
        c10.image(recommended_movie_posters[9])