from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('actors/', views.actor_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('actors/<int:pk>/', views.actor_detail),

    # review
    path('movies/<int:pk>/reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
    path('reviews/create/<int:movie_pk>/', views.review_create),

    # comment
    path('movies/<int:pk>/comments/', views.movie_comment_create),
    path('reviews/<int:pk>/comments/', views.review_comment_create),
    

]
