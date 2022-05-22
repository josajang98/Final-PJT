from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('wishlist/', views.wishlist_show_save),
]
