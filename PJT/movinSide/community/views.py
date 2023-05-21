from django.shortcuts import (get_list_or_404, get_object_or_404,
                               redirect , render)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Review, ReviewComment
from .serializers import ReviewCommentSerializer, ReviewDetailSerializer, ReviewListSerializer

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


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "GET":
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 리뷰 댓글 만들기
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data)

# 리뷰 댓글 삭제
@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def review_comment_delete(request, comment_pk):
    review_comment = get_object_or_404(ReviewComment, pk=comment_pk)
    if request.method == "DELETE":
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
