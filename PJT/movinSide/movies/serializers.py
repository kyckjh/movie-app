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
        fields = ("id", "name", "charater")

# 리뷰 리스트
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        
        fields = ("title", "content", 'like_users', 'comments', 'created_at', 'updated_at', )

# 영화 상세 조회
class MovieDetailSerializer(MovieListSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review = ReviewListSerializer(many=True, read_only=True)

    class Meta(MovieListSerializer.Meta):
        fields = '__all__'


# MovieListSerializer와 중복 되는 내용. 삭제 검토
class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", )

# 배우 상세 조회
class ActorDetailSerializer(ActorListSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta(ActorListSerializer.Meta):
        fields = ActorListSerializer.Meta.fields + (
            'movies',
        )

# 리뷰 상세 조회
class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

# 영화 댓글
class MovieCommentSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = MovieComment
        fields = ("content", "user", "movie",)

# 리뷰 댓글
class ReviewCommentSerializer(serializers.ModelSerializer):
    review = ReviewDetailSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = ("content", "user", "review",)

