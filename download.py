import streamlit as st
from pytube import YouTube
import shutil
import os
import requests

def download_file(link, user_path):
    st.write('Downloading...')
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    total_size = stream.filesize
    bytes_downloaded = 0

    with st.empty():
        progress_bar = st.progress(0)
        response = requests.get(stream.url, stream=True)
        with open(os.path.join(user_path, yt.title + '.mp4'), 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress = min(int(bytes_downloaded / total_size * 100), 100)
                    progress_bar.progress(progress)

    st.write('Download Complete! Download Another File...')

st.title('Youtube Video Downloader')

link = st.text_input("Enter Download Link:")
path = st.text_input("Enter Path For Download:")
st.write('E.g C->User->AppData')

if st.button("Download File"):
    if link.strip() == "" or path.strip() == "":
        st.error("Please enter both link and path.")
    else:
        download_file(link, path)
