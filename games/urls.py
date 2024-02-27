from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_games, name='games'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
    path('add/', views.add_game, name='add_game'),
    path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('remove/<int:game_id>/', views.remove_game, name='remove_game'),
]
