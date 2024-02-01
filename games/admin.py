from django.contrib import admin
from .models import Game, Category, Genre, Platform, Review


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'release_year',
        'image',
    )

    ordering = ('sku',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Game, GameAdmin)
admin.site.register(Category)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Platform)
admin.site.register(Review)

