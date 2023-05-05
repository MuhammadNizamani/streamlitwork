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
