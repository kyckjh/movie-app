from django.urls import path

from . import views

urlpatterns = [
    path('/', views.movie_list),
    path('actors/', views.actor_list),
    path('/<int:pk>/', views.movie_detail),
    path('actors/<int:pk>/', views.actor_detail),
    path('/<int:movie_pk>/like/', views.movie_likes),

    # comment
    path('/<int:movie_pk>/comment/', views.movie_comment_create),
    path('/comment/<int:comment_pk>/', views.movie_comment_delete),    
]
