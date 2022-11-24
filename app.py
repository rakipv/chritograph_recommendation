import streamlit as st
import pickle
import  pandas as pd

# here im implemnting recommendation defination method
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]

    for i in movies_list:
        movie_id= movies.iloc[i[0]].title

        recommended_movies.append(movies.iloc[i[0]].title)
    return    recommended_movies


movie_dict=pickle.load(open('C:/Users/rakip/PycharmProjects/christograph/venv/movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('C:/Users/rakip/PycharmProjects/christograph/venv/similarity.pkl','rb'))


st.title('Christograph')


selected_movie_name=st.selectbox(
    'Type or select from the dropdown',movies['title'].values)

if st.button('Recommend'):
    names=recommend(selected_movie_name)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #
    # with col2:
    #     st.text(names[1])
    #
    #
    # with col3:
    #     st.text(names[2])
    #
    # with col4:
    #     st.text(names[3])
    #
    # with col5:
    #     st.text(names[4])

    for i in names:

                 st.write(i)
