from django.shortcuts import (get_list_or_404, get_object_or_404,
                               redirect , render)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Actor, Movie, Review, MovieComment
from .serializers import (ActorDetailSerializer, ActorListSerializer,
                          MovieDetailSerializer, MovieListSerializer,
                          ReviewDetailSerializer, ReviewListSerializer,
                          MovieCommentSerializer, ReviewCommentSerializer)

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    review = get_list_or_404(Review)
    serializer = ReviewListSerializer(review, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    serializer = ActorDetailSerializer(actor)
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

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)
    

@permission_classes([IsAuthenticated])
@api_view(["POST"])
def movie_comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print('404')
        serializer.save(movie=movie)
        return Response(serializer.data)
    
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data)