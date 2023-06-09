from django.urls import path

from . import views

urlpatterns = [
    path('profile/<username>/', views.user_profile),
    path('follow/<username>/', views.follow),
    path('user/<int:pk>/', views.get_username),
]

