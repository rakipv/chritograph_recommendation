import time

import requests
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example

import numpy as  np
import streamlit as st
import webbrowser
from streamlit_lottie import st_lottie


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation_1 = "https://assets10.lottiefiles.com/packages/lf20_96bovdur.json"

lottie_anime_json = load_lottie_url(lottie_animation_1)

lottie_animation_2 = "https://assets8.lottiefiles.com/private_files/lf30_BQw8vE.json"

lottie_anime_json_2 = load_lottie_url(lottie_animation_2)


st.title('Welcome to Christograph')

st_lottie(lottie_anime_json, key="hello")

st.markdown('# With christograph, you can visualize extensive data in the form of graphs and nodes')

st_lottie(lottie_anime_json_2, key="humans")

st.markdown("### This is amazing right ")

url = 'https://bloom.neo4j.io/index.html?connectURL=neo4j%2Bs%3A%2F%2F5c360c8f.databases.neo4j.io&_ga=2.160532789.980640535.1669303345-1236140054.1667535849/'

if st.button('Bloom ne04j'):
    webbrowser.open_new_tab(url)

    st.balloons()