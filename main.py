import streamlit as st
import numpy as np
import pandas as pd
import time 
import seaborn as sns
import io
from utils import contains_dub
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objs as go
from genre import wordC, count_genre
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

st.markdown("<span style='font-size:25px;'><u>Heatmap of null values:</u></span>", unsafe_allow_html=True)
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
# st.set_option('deprecation.showPyplotGlobalUse', False)
st.write("")
st.write("")
st.markdown("<span style='font-size:23px;'>Anime are produce in japan so they original comes in japanese language so for USA anime comes in english dub so  i am going to remove that</span>", unsafe_allow_html=True)
anime_in_sub = df[~df['name'].str.contains('dub', case=False)]
st.dataframe(anime_in_sub.head(7))
buffer = io.StringIO()
anime_in_sub.info(buf = buffer)
s= buffer.getvalue()
st.text(s)
st.write("")
st.write("")
st.markdown("<span style='font-size:25px;'>Anime released in years 1960 to 2025</span>", unsafe_allow_html=True)

released = anime_in_sub["Released"]

# convert the "Released" column to a datetime format
released = pd.to_datetime(released, errors='coerce')

# extract the year from the datetime format and store it in a new column
anime_in_sub["year"] = released.dt.year
anime_per_year = anime_in_sub.groupby("year")["name"].count()
plt.bar(anime_per_year.index, anime_per_year.values)
plt.xlabel("Year")
plt.ylabel("Number of Anime Released")
plt.title("Anime Released Per Year")
plt.xlim(1960, 2025)
st.pyplot()
st.markdown("<span style='font-size:20px;'>Nowdays anime are populer so anime got more released nowdays</span>", unsafe_allow_html=True)
genres_text = wordC(anime_in_sub=anime_in_sub)
# create the WordCloud object
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(genres_text)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
st.pyplot()

# top10_counts = count_genre(genres_text)
# print(genres_text)
genre = []
list_of_genre = anime_in_sub['Genre'].tolist()
for num in range(len(list_of_genre)):
    a = str(list_of_genre[num]).split(",")
#     print(list_of_genre)
# print(a)
    for x in range(len(a)):
        genre.append(a[x])

print(genre)
genre = [x for x in genre if x != 'nan']
genre_series = pd.Series(genre)
# count frequency of each genre
genre_counts = genre_series.value_counts()

# Assuming you have a Pandas Series called 'genre_counts'
top_genres = genre_counts.sort_values(ascending=False)[:10] # Get top 10 genres

fig = go.Figure(data=[go.Bar(
            x=top_genres.values,
            y=top_genres.index,
            orientation='h'
)])

fig.update_layout(title="Top 10 Genres",
                  xaxis_title="Count",
                  yaxis_title="Genre")

st.plotly_chart(fig, use_container_width=True)


 