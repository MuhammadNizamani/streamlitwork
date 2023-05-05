import streamlit as st
import numpy as np
import pandas as pd
import time 
import seaborn as sns
df = pd.read_csv("animedata.csv")
st.text_input("Enter the number of of row you wants to see",10, key="number")
head = df.head(int(st.session_state.number))
st.markdown("<span style='font-size:25px;'>This dataset is taken from website name gogoanimes</span>", unsafe_allow_html=True)
st.dataframe(head)
st.markdown("<span style='font-size:25px;'>About field in this dataset</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:25px;'>There are 7 field</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Name of the Anime</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Type of name anime (Type of anime mean is it TV show, or ova, or spring name etc)</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>plot summary of anime</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Genre of Anime (Genre e.g comedy, romence, adventure, etc)</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Status of anime mean this anime is completed or continue or upcoming</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Other name: In anime word anime has usually anime has one japanese name and other english name . E.G Attack on Titan other name Shingeki no Kyojin</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size:17px;'>Released: year in which anime got released</span>", unsafe_allow_html=True)
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
# st.set_option('deprecation.showPyplotGlobalUse', False)