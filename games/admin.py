from django.contrib import admin
from .models import Game, Category, Genre, Platform, Reviews

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Reviews)

