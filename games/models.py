from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Reviews




class Game(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True , on_delete=models.SET_NULL)
    reviews = models.ForeignKey('Reviews', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    platform = models.CharField(null=True, blank=True)
    release_date = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name


