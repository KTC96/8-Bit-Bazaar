import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from django.shortcuts import get_object_or_404
from games.models import Game
from profiles.models import UserProfile
from django.utils import timezone
from django.contrib.auth.models import User



class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
            """
            Generate a random, unique order number using UUID
            """
            return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        if hasattr(self.game, 'discounted_price') and self.game.discounted_price is not None:
            self.lineitem_total = self.game.discounted_price * self.quantity
        else:
            self.lineitem_total = self.game.price * self.quantity 

        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.game.sku} on order {self.order.order_number}'

class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    for_new_users = models.BooleanField(default=False)

    def is_valid(self, is_new_user):
        """Check if the discount code is valid based on the start and end dates and user type."""
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date and (not self.for_new_users or is_new_user)

class AppliedDiscount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)