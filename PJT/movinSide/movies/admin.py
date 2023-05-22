from django.contrib import admin

from .models import Actor, Movie
from community.models import Review

# Register your models here.
admin.site.register((Movie, Actor, Review))