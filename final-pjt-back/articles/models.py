from django.db import models
from django.conf import settings

# Create your models here.

class Review(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    movie_id = models.IntegerField()

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')

    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



