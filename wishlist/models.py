from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    games = models.ManyToManyField('games.Game', related_name='wishlist_games')

    def __str__(self):
        return f"Wishlist for {self.user.username}"

        