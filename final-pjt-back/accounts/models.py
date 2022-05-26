from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    genre_id = models.IntegerField(default=0)


class WishList(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_wish = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    movie_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)

