import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud
from genre import wordC, wordforgraph


def heatmap(df):
    fig = px.imshow(df.isnull(), color_continuous_scale='Viridis')
    fig.update_layout(title='Missing Data Heatmap')
    fig.update_xaxes(title='Columns')
    fig.update_yaxes(title='Rows')
    return fig







def released_bar(anime_in_sub):
    released = anime_in_sub["Released"]

# convert the "Released" column to a datetime format
    released = pd.to_datetime(released, errors='coerce')

# extract the year from the datetime format and store it in a new column
    anime_in_sub["year"] = released.dt.year
    anime_per_year = anime_in_sub.groupby("year")["name"].count().reset_index()

# plot using Plotly
    fig = px.bar(anime_per_year, x="year", y="name", labels={"year": "Year", "name": "Number of Anime Released"})
    fig.update_layout(title="Anime Released Per Year", xaxis=dict(range=[1960, 2025]))
    return fig







def wordcloud_graph(anime_in_sub):
    genres_text = wordC(anime_in_sub=anime_in_sub)
# create the WordCloud object
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(genres_text)

    fig = go.Figure(go.Image(z=wordcloud.to_array()))

# set the axis to be invisible
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
    fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

# set the layout to be tight and remove the margin
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), autosize=True)
    return fig






def top10_genre(anime_in_sub):

    genre = wordforgraph(anime_in_sub=anime_in_sub)
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
    return fig

def least10_genre(anime_in_sub):
    genre = wordforgraph(anime_in_sub=anime_in_sub)
    genre_series = pd.Series(genre)
    genre_counts = genre_series.value_counts()

    # Assuming you have a Pandas Series called 'genre_counts'
    top_genres = genre_counts.sort_values(ascending=True)[:10] # Get top 10 genres

    fig = go.Figure(data=[go.Bar(
                x=top_genres.values,
                y=top_genres.index,
                orientation='h'
    )])

    fig.update_layout(title="least 10 Genres",
                    xaxis_title="Count",
                    yaxis_title="Genre")
    return fig



def top20_genre(anime_in_sub):
    genre = wordforgraph(anime_in_sub=anime_in_sub)
    genre_series = pd.Series(genre)
    genre_counts = genre_series.value_counts()
    sorted_counts = genre_counts.sort_values(ascending=False)
    top10_counts = sorted_counts.head(20)

    fig = px.pie(values=top10_counts.values, names=top10_counts.index, title='Top 20 Genres')
    return fig




def top10tpye(anime_in_sub):
    # count frequency of each anime type
    type_counts = anime_in_sub['Type'].value_counts()

    # sort in descending order
    sorted_counts = type_counts.sort_values(ascending=False)

    # take top 10
    top10_counts = sorted_counts.head(10)

# plot as bar chart
    fig = px.bar(x=top10_counts.index, y=top10_counts.values, labels={'x': 'Anime Type', 'y': 'Count'}, title='Top 10 Anime Types')
    return fig

def status(anime_in_sub):
    status_counts = anime_in_sub.groupby('Status').size()

    # create a bar chart of the status counts using Plotly
    fig = go.Figure(data=[go.Bar(x=status_counts.index, y=status_counts.values)])

    # set the chart title and axis labels
    fig.update_layout(title='Anime Status', xaxis_title='Status', yaxis_title='Count')
    return fig