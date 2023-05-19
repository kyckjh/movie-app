from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.


def some_view_func(request):
    token = Token.objects.create(user=...)
    return Response({'token': token.key})

@api_view(['GET'])
def user_profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@api_view(['POST'])
def follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
            followed = False
        else:
            user.followers.add(request.user)
            followed = True
    context = {
        'followed' : followed,
    }
    serializer = UserSerializer(user)
    return Response(serializer.data)