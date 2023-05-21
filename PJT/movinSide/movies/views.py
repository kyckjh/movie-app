from django.shortcuts import (get_list_or_404, get_object_or_404,
                               redirect , render)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Actor, Movie, MovieComment
from .serializers import (ActorDetailSerializer, ActorListSerializer,
                          MovieDetailSerializer, MovieListSerializer,
                          MovieCommentSerializer,)

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
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)
    
# 영화 댓글 만들기
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def movie_comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)
    
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