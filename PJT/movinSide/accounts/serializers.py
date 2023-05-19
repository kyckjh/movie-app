from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from movies.serializers import MovieListSerializer
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ("id", "title", )

    like_movies = MovieListSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "like_movies",  'profile_img', "followers", "followings",)

        #  "followes", "followings", 

class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'id')
