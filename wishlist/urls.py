from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name="wishlist"),
    path('add/<int:game_id>/', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove/<int:game_id>/', views.remove_from_wishlist, name="remove_from_wishlist"),
    path('add_to_bag/<int:game_id>/', views.add_to_bag_wishlist, name="add_to_bag_wishlist"),
]
