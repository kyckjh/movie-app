from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.


def some_view_func(request):
    token = Token.objects.create(user=...)
    return Response({'token': token.key})