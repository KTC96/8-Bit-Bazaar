import json

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem
from games.models import Game
from bag.contexts import bag_contents
from .forms import OrderForm

import stripe



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    game = Game.objects.get(id=item_id)
                    quantity = item_data
                    order_line_item = OrderLineItem(
                        order=order,
                        game=game,
                        quantity=item_data,
                    )
                    order_line_item.save()

                except Game.DoesNotExist:
                    messages.error(request, (
                        "We couldn't locate one of the games from your bag in our database."
                        " Please reach out to us for help!")
                    )
                    order.delete()

            request.session ['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number] ))
        else:
            messages.error(request, 'Oops! There was an error with your form. \
                Please double check your information.')


    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag currently lacks any old-school games.")
            return redirect(reverse('games'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total *100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        print(intent)
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle view after a successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    
    messages.success(request, f'Order successfuly processed!\
        Your order number is {order_number}. A confirmation email \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }

    return render(request, template, context)



