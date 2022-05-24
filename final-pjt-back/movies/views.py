from django.shortcuts import render
import requests


import requests
import json


def get_movie_datas():
    total_data = []
    base_url = ' https://api.themoviedb.org/3/movie/popular'
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for page in range(1, 4):
        params ={
            'api_key' : '',
            'language':'ko',
            'page' : '{}'.format(page),
            'resion' : 'KR'
        }
        movies = requests.get(base_url, params = params).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path']
                }
                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }
                total_data.append(data)

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)
