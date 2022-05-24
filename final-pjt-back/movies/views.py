from django.shortcuts import render
from pprint import pprint
import requests

'''
제거해줘야함
'adult': False,
'genre_ids': [28, 878, 14],
'video': False,
'vote_average': 6.4,
'''

# Create your views here.
# base_url = ' https://api.themoviedb.org/3/movie/popular'
# for page in range(1,3):
#     params ={
#         'api_key' : '50ca281a943ecad26f13d17bc9d40827',
#         'language':'ko',
#         'page' : '{}'.format(page),
#         'resion' : 'KR'
#     }
#     res = requests.get(base_url, params = params).json()
#     results = res['results']
#     for result in results:
#         pass



import requests
import json

TMDB_API_KEY = '50ca281a943ecad26f13d17bc9d40827'

def get_movie_datas():
    total_data = []
    base_url = ' https://api.themoviedb.org/3/movie/popular'
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for page in range(1, 4):
        params ={
            'api_key' : '50ca281a943ecad26f13d17bc9d40827',
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

get_movie_datas()
