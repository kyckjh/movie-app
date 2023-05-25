from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list),
    path('actors/', views.actor_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('<int:movie_pk>/like/', views.movie_likes),
    path('recommend/', views.recommend),

    # comment
    path('<int:movie_pk>/comments/', views.movie_comment_list_or_create),\
    path('comment/<int:comment_pk>/', views.movie_comment_delete),    

]
