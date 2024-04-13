import time
import json

from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

import stripe

from .models import Order, OrderLineItem
from games.models import Game

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        email_subject = render_to_string(
            'checkout/emails/confirmation_email_subject.txt',
            {'order': order}
        )
        email_body = render_to_string(
            'checkout/emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(intent.charges.data[0].id)

        billing_details = stripe_charge.billing_details
        
        total = round(stripe_charge.amount / 100, 2)

        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        user_profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = User.objects.get(username=username)

            if save_info:
                user_profile.default_phone_number = billing_details.phone
                user_profile.default_country = billing_details.address.country
                user_profile.default_postcode = billing_details.address.postal_code
                user_profile.default_town_or_city = billing_details.address.city
                user_profile.default_street_address1 = billing_details.address.line1
                user_profile.default_street_address2 = billing_details.address.line2
                user_profile.default_county = billing_details.address.state
                user_profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    email__iexact=billing_details.email,
                    total=total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=user_profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid
                )
                for item_id, item_data in json.loads(bag).items():
                    game = Game.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200)
