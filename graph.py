import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

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