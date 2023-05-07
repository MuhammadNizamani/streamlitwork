import streamlit as st
import pandas as pd
import io
from graph import heatmap, released_bar, wordcloud_graph, top10_genre, least10_genre, top20_genre, top10tpye, status
sidebar = st.sidebar.selectbox("", [])

# write text in sidebar
# if sidebar == "Intro":
st.sidebar.markdown("<span style='font-size:30px;'>Dataset Details</span>", unsafe_allow_html=True)

st.sidebar.markdown("<span style='font-size:25px;'>Introduction</span>", unsafe_allow_html=True)
st.sidebar.write('In this EDA dataset of anime taken from kaggle.')
st.sidebar.write('There are 7 field and see detail by selecting diffrent option of Navigation.')
# elif sidebar == "Name":
st.sidebar.markdown("<span style='font-size:25px;'>Name</span>", unsafe_allow_html=True)
st.sidebar.write("Name of anime in English")
# elif sidebar == "Type":
st.sidebar.markdown("<span style='font-size:25px;'>Type</span>", unsafe_allow_html=True)
st.sidebar.write("Type of name anime (Type of anime mean is it TV show, or ova, or spring name etc)")
# elif sidebar == 'Plot Summary':
st.sidebar.markdown("<span style='font-size:25px;'>Plot Summary</span>", unsafe_allow_html=True)
st.sidebar.write("Anime's main stroy line in paragraph")
# elif sidebar == 'Genre':
st.sidebar.markdown("<span style='font-size:25px;'>Genre</span>", unsafe_allow_html=True)
st.sidebar.write("Genre of Anime (Genre e.g comedy, romence, adventure, etc)")
# elif sidebar == 'Released':
st.sidebar.markdown("<span style='font-size:25px;'>Released</span>", unsafe_allow_html=True)
st.sidebar.write("Released: year in which anime got released")
# elif sidebar == "Status":
st.sidebar.markdown("<span style='font-size:25px;'>Status</span>", unsafe_allow_html=True)
st.sidebar.write("Status of anime mean this anime is completed or continue or upcoming")
# elif sidebar == 'Other Name':
st.sidebar.markdown("<span style='font-size:25px;'>Other Name</span>", unsafe_allow_html=True)
st.sidebar.write("Other name: In anime word anime has usually anime has one japanese name and other english name . E.G Attack on Titan other name Shingeki no Kyojin")


st.markdown("<span style='font-size:40px;text-align: center;'>EDA of Anime dataset</span>", unsafe_allow_html=True)

df = pd.read_csv("animedata.csv")
st.markdown("<span style='font-size:25px;'>Enter the number of of row you wants to see</span>", unsafe_allow_html=True)
st.text_input("",10, key="number")
head = df.head(int(st.session_state.number))
st.markdown("<span style='font-size:25px;'>This dataset is taken from website name gogoanimes</span>", unsafe_allow_html=True)
st.dataframe(head)

st.markdown("<span style='font-size:25px;'><u>Heatmap of null values:</u></span>", unsafe_allow_html=True)
fig = heatmap(df= df)
st.plotly_chart(fig)

st.write("")
st.write("")
st.markdown("<span style='font-size:23px;'>Anime are produce in japan so they original comes in japanese language so for USA anime comes in english dub so  i am going to remove that</span>", unsafe_allow_html=True)
anime_in_sub = df[~df['name'].str.contains('dub', case=False)]
st.dataframe(anime_in_sub.head(7))
#for info function to show on streamlit
buffer = io.StringIO()
anime_in_sub.info(buf = buffer)
s= buffer.getvalue()
st.text(s)
st.write("\n\n")
st.markdown("<span style='font-size:25px;'>Anime released in years 1960 to 2025</span>", unsafe_allow_html=True)


fig = released_bar(anime_in_sub=anime_in_sub)
st.plotly_chart(fig)
st.markdown("<span style='font-size:21px;'>Anime are getting more released in 2010 to 2022 becasue of internet anime got more audience </span>", unsafe_allow_html=True)
st.write("\n\n\n\n")
#wordcloud
fig = wordcloud_graph(anime_in_sub=anime_in_sub)
st.plotly_chart(fig)

fig = top10_genre(anime_in_sub=anime_in_sub)
st.plotly_chart(fig, use_container_width=True)

fig = least10_genre(anime_in_sub=anime_in_sub)
st.plotly_chart(fig, use_container_width=True)

fig = top20_genre(anime_in_sub=anime_in_sub)
st.plotly_chart(fig)

fig  = top10tpye(anime_in_sub=anime_in_sub)
st.plotly_chart(fig, use_container_width=True)

# status_counts = anime_in_sub.groupby('Status').size()

# # create a bar chart of the status counts using Plotly
# fig = go.Figure(data=[go.Bar(x=status_counts.index, y=status_counts.values)])

# # set the chart title and axis labels
# fig.update_layout(title='Anime Status', xaxis_title='Status', yaxis_title='Count')

# display the chart
fig = status(anime_in_sub=anime_in_sub)

st.plotly_chart(fig, use_container_width=True)


# create a sample dataframe
