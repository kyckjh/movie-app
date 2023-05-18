from rest_framework import serializers

from .models import Actor, Movie, Review, MovieComment, ReviewComment

# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "overview")

# 영화 배우 리스트
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "name")

# 리뷰 리스트
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("title", "content")

# 영화 상세 조회
class MovieDetailSerializer(MovieListSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review = ReviewListSerializer(many=True, read_only=True)

    class Meta(MovieListSerializer.Meta):
        fields = '__all__'


class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)

class ActorDetailSerializer(ActorListSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta(ActorListSerializer.Meta):
        fields = ActorListSerializer.Meta.fields + (
            'movies',
        )

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class MoviewCommentSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = MovieComment
        fields = ("content", "user",)

class ReviewCommentSerializer(serializers.ModelSerializer):
    review = ReviewDetailSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = ("content", "user",)

