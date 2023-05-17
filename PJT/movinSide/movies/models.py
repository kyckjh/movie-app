from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=10)
    overview = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    actors = models.ManyToManyField(Actor, related_name='movies')

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)


