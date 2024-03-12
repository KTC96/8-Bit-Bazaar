from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_games, name='games'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
    path('add/', views.add_game, name='add_game'),
    path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('remove/<int:game_id>/', views.remove_game, name='remove_game'),
    path('add_review/<int:game_id>/', views.add_review, name='add_review'),
    path(
        'edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path(
        'delete_review/<int:review_id>/', views.delete_review,
        name='delete_review'
    ),
    path('all_reviews/', views.all_reviews, name='all_reviews'),
]
