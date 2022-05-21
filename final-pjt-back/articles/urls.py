from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/', views.review_list_create),
    path('<int:movie_pk>/update/<int:review_pk>/', views.review_update),
]