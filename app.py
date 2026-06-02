import streamlit as st
import pickle
import pandas as pd
import requests
from huggingface_hub import hf_hub_download

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1 {
    color: #E50914;
    text-align: center;
    font-size: 55px;
    font-family: sans-serif;
}

.stButton>button {
    background-color: #E50914;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 220px;
    font-size: 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: white;
    color: #E50914;
    transform: scale(1.05);
}

div[data-baseweb="select"] > div {
    background-color: #262730;
    color: white;
    border-radius: 10px;
}

img {
    border-radius: 15px;
    transition: 0.3s;
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px red;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1>🎬 Movie Recommender System</h1>",
    unsafe_allow_html=True
)

# ---------------- LOAD DATA FROM HUGGING FACE ----------------
@st.cache_resource(show_spinner="🎬 Loading recommendation engine...")
def load_artifacts():
    movies_path = hf_hub_download(
        repo_id="shanke3120/movie_recommender_system",
        filename="movie_list.pkl",
        repo_type="dataset"
    )
    similarity_path = hf_hub_download(
        repo_id="shanke3120/movie_recommender_system",
        filename="similarity.pkl",
        repo_type="dataset"
    )
    with open(movies_path, "rb") as f:
        movies = pickle.load(f)
    with open(similarity_path, "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity

movies, similarity = load_artifacts()

# ---------------- FETCH POSTER FUNCTION ----------------
def fetch_poster(movie_id):
    api_key = "8bb840652fb00fcbcb85cf58e701d79c"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ---------------- DROPDOWN ----------------
selected_movie_name = st.selectbox(
    "🎬 Select a movie",
    movies['title'].values
)

# ---------------- BUTTON ----------------
if st.button('Recommend'):

    st.snow()

    names, posters = recommend(selected_movie_name)

    st.success("Movies Recommended Successfully ✅")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.markdown(f"<h4 style='text-align:center; color:white;'>{names[0]}</h4>", unsafe_allow_html=True)

    with col2:
        st.image(posters[1])
        st.markdown(f"<h4 style='text-align:center; color:white;'>{names[1]}</h4>", unsafe_allow_html=True)

    with col3:
        st.image(posters[2])
        st.markdown(f"<h4 style='text-align:center; color:white;'>{names[2]}</h4>", unsafe_allow_html=True)

    with col4:
        st.image(posters[3])
        st.markdown(f"<h4 style='text-align:center; color:white;'>{names[3]}</h4>", unsafe_allow_html=True)

    with col5:
        st.image(posters[4])
        st.markdown(f"<h4 style='text-align:center; color:white;'>{names[4]}</h4>", unsafe_allow_html=True)
