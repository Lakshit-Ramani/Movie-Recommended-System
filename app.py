import streamlit as st
import pickle
import pandas as pd

# 1. Custom Recommendation Logic utilizing the compressed dictionary format
def recommend(movie):
    # Find the matching dataframe row index for the target title
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Directly pull the precomputed list of top 5 similar movie indices from our dictionary
    recommended_movie_indices = similarity[movie_index]
    
    recommended_movie_names = []
    for i in recommended_movie_indices:
        # Resolve indices back into clean string movie titles
        recommended_movie_names.append(movies.iloc[i].title)
        
    return recommended_movie_names

# 2. Main Page Header Layout
st.header('Movie Recommender System')

# 3. Secure Caching Load (Make sure these names exactly match your exported filenames!)
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity_dict.pkl', 'rb'))

# 4. Handle User Input Selection Elements
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# 5. Execution State Handler
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    st.markdown("### 🎬 Recommended Movies")
    
    # Build clean horizontal 5-column dashboard partitions
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
                    min-height: 120px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                ">
                    🎥 {recommended_movie_names[idx]}
                </div>
                """,
                unsafe_allow_html=True
            )