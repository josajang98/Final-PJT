from django.urls import path
from . import views

urlpatterns = [
    path('<username>/profile/', views.profile),
    path('<username>/profile/<int:genre_pk>/', views.profile_change_genre),
    path('wishlist/', views.wishlist_show_save),
]
