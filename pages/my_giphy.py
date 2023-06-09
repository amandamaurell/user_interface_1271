import requests
import streamlit as st

url = "https://api.giphy.com/v1/gifs/random"

gif = st.text_input("Tell me what gif you would like to see...", value='dog')


params={
    'api_key':st.secrets.giphy_api_key.API_KEY_2,
    'tag':gif
}

response = requests.get(url, params=params).json()

giphy = response['data']["embed_url"]

st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)
