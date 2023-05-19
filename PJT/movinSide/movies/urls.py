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
    path('movies/<int:movie_pk>/comment/', views.movie_comment_create),
    path('movies/comment/<int:comment_pk>/', views.movie_comment_delete),

    path('reviews/<int:review_pk>/comment/', views.review_comment_create),
    path('reviews/comment/<int:comment_pk>/', views.review_comment_delete),
    
]
