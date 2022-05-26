from django.db import models
from django.forms import BooleanField, CharField

# Create your models here.
''' 
제거해줘야함
'adult': False,
'genre_ids': [28, 878, 14],
'video': False,
'vote_average': 6.4,
'''

class Movie(models.Model):
    movie_id            = models.IntegerField()
    overview            = models.TextField()
    popularity          = models.IntegerField()
    poster_path         = models.CharField(max_length=200)
    released_date        = models.DateField()
    title               = models.CharField(max_length=100)

