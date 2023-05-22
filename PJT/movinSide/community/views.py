from django.shortcuts import (get_list_or_404, get_object_or_404,
                               redirect , render)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Review, ReviewComment
from .serializers import ReviewCommentSerializer, ReviewDetailSerializer, ReviewListSerializer
from movies.models import Movie

# Create your views here.
@api_view(['GET'])
def review_list(request):
    review = get_list_or_404(Review)
    serializer = ReviewListSerializer(review, many=True)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)

# 리뷰 상세 조회, 업데이트, 삭제    
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    def review_detail():
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    def review_update():
        if request.user == review.user:
            serializer = ReviewDetailSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    def review_delete():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "GET":
        return review_detail()
    if request.method == "PUT":
        return review_update()
    elif request.method == "DELETE":
        return review_delete()

# 리뷰 댓글 만들기
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def review_comment_list_or_create(request, review_pk):
    def comment_list():
        comments = get_list_or_404(ReviewComment, review=review_pk)[:-1]
        serializer = ReviewCommentSerializer(comments, many=True)
        return Response(serializer.data)
    def create_comment():
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            comments = review.comments.all()
            serializer = ReviewCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        return comment_list()
    elif request.method == "POST":
        return create_comment()

# 리뷰 댓글 삭제
@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def review_comment_delete(request, comment_pk):
    review_comment = get_object_or_404(ReviewComment, pk=comment_pk)
    if request.method == "DELETE":
        if request.user == review_comment.user:
            review_comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# 리뷰 좋아요
@api_view(['POST'])
def review_likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
