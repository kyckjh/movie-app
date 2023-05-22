from rest_framework import serializers
from .models import Actor, Movie, MovieComment
from community.serializers import ReviewListSerializer


# 영화 배우 리스트
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "name", "character")

# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "overview")

# 영화 상세 조회
class MovieDetailSerializer(MovieListSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review = ReviewListSerializer(many=True, read_only=True)

    class Meta(MovieListSerializer.Meta):
        fields = '__all__'


# 배우 상세 조회
class ActorDetailSerializer(ActorListSerializer):
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta(ActorListSerializer.Meta):
        fields = ActorListSerializer.Meta.fields + (
            'movies',
        )


# 영화 댓글
class MovieCommentSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    class Meta:
        model = MovieComment
        fields = ("content", "user", "movie",)

class MovieCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = ('id', 'content', 'user')