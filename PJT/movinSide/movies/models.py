from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

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
    #actors = models.ManyToManyField(Actor, related_name='movies')

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)

