import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    st.markdown("### 🎬 Recommended Movies")
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for idx, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div style="
                    background-color: #1e1e2e;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 20px 10px;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                    color: #ffffff;
                    min-height: 100px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    🎥 {recommended_movie_names[idx]}
                </div>
                """,
                unsafe_allow_html=True
            )