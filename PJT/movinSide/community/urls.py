from django.urls import path
from . import views

urlpatterns = [

    # review
    path('movies/<int:pk>/reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
    path('reviews/create/<int:movie_pk>/', views.review_create),
    path('reviews/<int:review_pk>/like/', views.review_likes),

    # comment
    path('reviews/<int:review_pk>/comment/', views.review_comment_create),
    path('reviews/comment/<int:comment_pk>/', views.review_comment_delete),

]