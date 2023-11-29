import streamlit as st
import pandas as pd
from PIL import Image

st.subheader('Uploading the CSV file')
df = st.file_uploader('Upload CSV file: ',type = ['csv','xlsx'])
if df is not None:
    st.dataframe(df)

st.subheader('Loading the CSV file')
df = pd.read_csv('D:\Streamlit\Products.csv')
if df is not None:
    st.table(df.head())

st.subheader('Dealing with images directly')
image = Image.open('D:\Streamlit\img.png')
st.image(image)

st.subheader('Dealing with images with file uploader')
imageup = st.file_uploader('Upload image file: ',type = ['jpeg','png'])
if imageup is not None:
    st.image(imageup)

st.subheader('Dealing with videos with file uploader')
videoup = st.file_uploader('Upload video file: ',type = ['mp4','mkv'])
if videoup is not None:
    st.video(videoup, start_time = 0)

st.subheader('Dealing with audio with file uploader')
audioup = st.file_uploader('Upload audio file: ',type = ['mp3','wav'])
if audioup is not None:
    st.audio(audioup, start_time = 0)
