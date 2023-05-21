from rest_framework import serializers
from .models import Review, ReviewComment
from django.contrib.auth import get_user_model

User = get_user_model()

# 리뷰 리스트
# class MovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ("title", "overview")


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        
        fields = ("title", "content", 'like_users', 'comments', 'created_at', 'updated_at', )

# 리뷰 상세 조회
class ReviewDetailSerializer(serializers.ModelSerializer):
    # movie = MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

# 리뷰 댓글
class ReviewCommentSerializer(serializers.ModelSerializer):
    review = ReviewDetailSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = ("content", "user", "review",)

