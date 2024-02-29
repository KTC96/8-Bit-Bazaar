from django.db import models
from django.contrib.auth.models import User
from wishlist.models import Wishlist
class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Platform(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Game(models.Model):
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey('Category', null=True, blank=True , on_delete=models.SET_NULL)
    platform = models.ForeignKey('Platform', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    release_year = models.CharField(null=True, blank=True, max_length=100)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    wishlist = models.ManyToManyField('wishlist.Wishlist', blank=True, related_name='games_in_wishlist')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Review(models.Model):

    title = models.CharField(max_length=80)
    rating = models.DecimalField(decimal_places=1, max_digits=2, null=True)
    body = models.TextField()
    game = models.ForeignKey(Game, blank=False,  on_delete=models.CASCADE)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        unique_together = [['game', 'author']]
        ordering = ["-date"]

    def __str__(self):
          return f"{self.title} - {self.author.username}"

