import streamlit as st
import numpy as np
import pandas as pd
import io
# from utils import contains_dub
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objs as go
from genre import wordC
import plotly.express as px
sidebar = st.sidebar.selectbox('Dataset Detail', ['Intro', 'Name','Type','Plot Summary','Released', 'Genre', 'Status'])

# write text in sidebar
if sidebar == "Intro":
    st.sidebar.write('In this EDA dataset of anime taken from kaggle.')
    st.sidebar.write('There are 7 field and see detail by selecting diffrent option of Navigation.')
elif sidebar == "Name":
    st.sidebar.write("Name of anime in English")
elif sidebar == "Type":
    st.sidebar.write("Type of name anime (Type of anime mean is it TV show, or ova, or spring name etc)")
elif sidebar == 'Plot Summary':
    st.sidebar.write("Anime's main stroy line in paragraph")
st.markdown("<span style='font-size:40px;text-align: center;'>EDA of Anime dataset</span>", unsafe_allow_html=True)

df = pd.read_csv("animedata.csv")
st.markdown("<span style='font-size:25px;'>Enter the number of of row you wants to see</span>", unsafe_allow_html=True)
st.text_input("",10, key="number")
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
fig = px.imshow(df.isnull(), color_continuous_scale='Viridis')
fig.update_layout(title='Missing Data Heatmap')
fig.update_xaxes(title='Columns')
fig.update_yaxes(title='Rows')

st.plotly_chart(fig)

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
anime_per_year = anime_in_sub.groupby("year")["name"].count().reset_index()

# plot using Plotly
fig = px.bar(anime_per_year, x="year", y="name", labels={"year": "Year", "name": "Number of Anime Released"})
fig.update_layout(title="Anime Released Per Year", xaxis=dict(range=[1960, 2025]))
st.plotly_chart(fig)
st.markdown("<span style='font-size:21px;'>Anime are getting more released in 2010 to 2022 becasue of internet anime got more audience </span>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
genres_text = wordC(anime_in_sub=anime_in_sub)
# create the WordCloud object
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(genres_text)

fig = go.Figure(go.Image(z=wordcloud.to_array()))

# set the axis to be invisible
fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

# set the layout to be tight and remove the margin
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), autosize=True)

# display the Plotly figure
st.plotly_chart(fig)
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

# print(genre)
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

genre_counts = genre_series.value_counts()

# Assuming you have a Pandas Series called 'genre_counts'
top_genres = genre_counts.sort_values(ascending=True)[:10] # Get top 10 genres

fig = go.Figure(data=[go.Bar(
            x=top_genres.values,
            y=top_genres.index,
            orientation='h'
)])

fig.update_layout(title="10 Genres least genre",
                  xaxis_title="Count",
                  yaxis_title="Genre")

st.plotly_chart(fig, use_container_width=True)

genre_series = pd.Series(genre)
genre_counts = genre_series.value_counts()
sorted_counts = genre_counts.sort_values(ascending=False)
top10_counts = sorted_counts.head(20)

fig = px.pie(values=top10_counts.values, names=top10_counts.index, title='Top 20 Genres')
st.plotly_chart(fig)

# count frequency of each anime type
type_counts = anime_in_sub['Type'].value_counts()

# sort in descending order
sorted_counts = type_counts.sort_values(ascending=False)

# take top 10
top10_counts = sorted_counts.head(10)

# plot as bar chart
fig = px.bar(x=top10_counts.index, y=top10_counts.values, labels={'x': 'Anime Type', 'y': 'Count'}, title='Top 10 Anime Types')
st.plotly_chart(fig, use_container_width=True)
status_counts = anime_in_sub.groupby('Status').size()

# create a bar chart of the status counts using Plotly
fig = go.Figure(data=[go.Bar(x=status_counts.index, y=status_counts.values)])

# set the chart title and axis labels
fig.update_layout(title='Anime Status', xaxis_title='Status', yaxis_title='Count')

# display the chart

st.plotly_chart(fig, use_container_width=True)


# create a sample dataframe
