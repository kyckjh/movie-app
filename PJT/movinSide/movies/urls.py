from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('actors/', views.actor_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('actors/<int:pk>/', views.actor_detail),
    path('movies/<int:movie_pk>/like/', views.movie_likes),

    # comment
    path('movies/<int:movie_pk>/comment/', views.movie_comment_create),
    path('movies/comment/<int:comment_pk>/', views.movie_comment_delete),    
]
