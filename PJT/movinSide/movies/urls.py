from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('actors/', views.actor_list),
    path('reviews/', views.review_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('actors/<int:pk>/', views.actor_detail),
    path('reviews/<int:pk>/', views.review_detail),

    path('reviews/create/<int:pk>/', views.review_create),
    

]
