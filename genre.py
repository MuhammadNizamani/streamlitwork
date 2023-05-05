import pandas as pd
def wordC(anime_in_sub):
    genre = []
    list_of_genre = anime_in_sub['Genre'].tolist()
    for num in range(len(list_of_genre)):
        a = str(list_of_genre[num]).split(",")
    #     print(list_of_genre)
    # print(a)
        for x in range(len(a)):
            genre.append(a[x])
    genre = [x for x in genre if x != 'nan']
    genres_text = ' '.join(genre)
    return genres_text

def count_genre(genre):
    genre_series = pd.Series(genre)

# count frequency of each genre
    genre_counts = genre_series.value_counts()

# sort in descending order
    sorted_counts = genre_counts.sort_values(ascending=False)

# take top 10
    top10_counts = sorted_counts.head(10)
    return top10_counts

