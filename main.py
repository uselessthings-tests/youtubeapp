import streamlit as st 
from pytube import YouTube
import pyshorteners

shorten = pyshorteners.Shortener()

st.set_page_config("Youtube Converter" , page_icon="https://img.icons8.com/color/48/000000/youtube-play.png")

st.title("Youtube Converter")
textbox = st.text_input('Enter the video link', 'Video link')

option = st.selectbox(
    'To what format would you like to convert the video',
    ('MP4', 'MP3'))

if st.button('Convert'):
    if option == 'MP4':
        video_parse = YouTube(textbox)
        video_with_audio_hd  = str(video_parse.vid_info).split("'itag': 22,")[1].split(", 'mimeType':")[0].replace("'url': '"," ").replace("'","").replace(" ","")
        st.write("Your video is ready to be downloaded \n visit this link to download the video 👇")
        st.write(shorten.tinyurl.short(video_with_audio_hd))

    if option == 'MP3':
        video_parse = YouTube(textbox)
        video_audio = video_parse.streams.filter(only_audio=True).first().url
        st.write("Your audio is ready to be downloaded \n visit this link to download the video 👇")
        st.write(shorten.tinyurl.short(video_audio))


