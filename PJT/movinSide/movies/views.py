from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Actor, Movie, MovieComment
from .serializers import (ActorDetailSerializer, ActorListSerializer,
                          MovieCommentListSerializer, MovieCommentSerializer,
                          MovieDetailSerializer, MovieListSerializer)

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
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)
    
# 영화 댓글 조회 및 만들기
@permission_classes([IsAuthenticated])  
@api_view(["GET","POST"])
def movie_comment_list_or_create(request, movie_pk):
    def comment_list():
        movie = get_object_or_404(Movie, pk=movie_pk)
        comments = get_list_or_404(MovieComment, movie=movie)[::-1]
        serializer = MovieCommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    def create_comment():
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == "GET":
        return comment_list()
    elif request.method == "POST":
        return create_comment()
    
# 영화 댓글 삭제
@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def movie_comment_delete(request, comment_pk):
    movie_comment = get_object_or_404(MovieComment, pk=comment_pk)
    if request.method == "DELETE":
        movie_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# 영화 좋아요
@api_view(['POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)