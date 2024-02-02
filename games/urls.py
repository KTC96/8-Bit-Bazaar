from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_games, name='games'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
]