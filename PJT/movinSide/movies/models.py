from django.db import models
from django.conf import settings


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    image_path = models.TextField(null=True)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=10)
    overview = models.TextField()
    content = models.TextField()
    release_date = models.TextField()
    original_language = models.CharField(max_length=10)
    original_title = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    actor_ids = models.ManyToManyField(Actor, related_name='movies')

# class Review(models.Model):
#     title = models.CharField(max_length=100)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.TextField()
#     movie = models.ForeignKey(
#         Movie, related_name='reviews', on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class MovieComment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

