from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/reviews/', views.review_list_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_delete),
    path('<int:movie_pk>/like/<int:review_pk>/', views.like_review),
    path('genrewc/<int:genre_pk>/', views.genre_save),
]