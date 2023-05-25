#from django.contrib.auth import get_user_model
# from accounts.models import User
from rest_framework import serializers

from .models import Review, ReviewComment

# from movies.serializers import MovieListSerializer


#User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('pk','username',)


# 리뷰 리스트
class ReviewListSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ("title", "content", 'like_users', 'comments', 'created_at', 'updated_at', 'user')

# 리뷰 상세 조회
class ReviewDetailSerializer(serializers.ModelSerializer):
    # movie = movies.serializers.MovieListSerializer(read_only=True)
    # movie = MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

        def movie_serializer(self):
            from movies.serializers import MovieListSerializer
            return MovieListSerializer(read_only=True)

# 리뷰 댓글
class ReviewCommentSerializer(serializers.ModelSerializer):
    review = ReviewDetailSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = ("content", "user", "review",)

