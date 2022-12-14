import pickle
import streamlit as st
import requests
import pandas as pd
import webbrowser
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Journal recommender system",
    page_icon="🕸",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "## A content based Journal recommendation system build using cosine similarity"
    }
)


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


<<<<<<< HEAD
lottie_animation_1 = "https://assets6.lottiefiles.com/packages/lf20_zrqthn6o.json"

lottie_anime_json = load_lottie_url(lottie_animation_1)
st.title('Welcome to Christograph Recommender')
=======
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
>>>>>>> 0bb1abb12d1f75820e9b7dbe1c21a5565084a4e2

st_lottie(lottie_anime_json, key="hello" , width=600)

lottie_animation_2 = "https://assets8.lottiefiles.com/packages/lf20_dyrstm8f.json"

lottie_anime_json_2 = load_lottie_url(lottie_animation_2)

st.markdown('#  Confused on whom to approach for research or specialization among many faculty? ')

st_lottie(lottie_anime_json_2, key="humans", width=500)

lottie_animation_3 = "https://assets3.lottiefiles.com/packages/lf20_ldf6z8do.json"
lottie_anime_json_3 = load_lottie_url(lottie_animation_3)
st.markdown('#  Dont worry Christograph AI Recommendation got you ')
st_lottie(lottie_anime_json_3, key="a", width=500)
st.header('Journal Recommender System')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


function_option = st.sidebar.selectbox("Select The Funtionality: ", [
    "Get recommendations by Journal name", "Get recommendations by Journal Author"])
if function_option == "Get recommendations by Journal name":
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)),
                             reverse=True, key=lambda x: x[1])[1:6]
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in movies_list:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters


    movies_dict = pickle.load(open('R:/react_voice/chritograph_recommendation/data/movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('R:/react_voice/chritograph_recommendation/similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a Journal from the dropdown",
        movie_list)

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(
            selected_movie)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        col4, col5 = st.columns(2)
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

if function_option == "Get recommendations by Journal Author":
    def recommend_director(director):
        movie_index = movies[movies['crew'] == director].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)),
                             reverse=True, key=lambda x: x[1])[1:6]
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in movies_list:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters


    movies_dict = pickle.load(open('R:/react_voice/chritograph_recommendation/data/movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('R:/react_voice/chritograph_recommendation/similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    director = movies['crew'].values
    selected_movie = st.selectbox(
        "Type or select a Journal from the dropdown",
        director)

    if st.button('Get Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend_director(
            selected_movie)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        col4, col5 = st.columns(2)
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

movies_dict = pickle.load(open('R:/react_voice/chritograph_recommendation/data/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('R:/react_voice/chritograph_recommendation/similarity.pkl', 'rb'))

movie_list = movies['title'].values
director = movies['crew'].values
