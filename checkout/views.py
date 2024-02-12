from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag currently lacks any old-school games.")
        return redirect(reverse('games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OVcWCFITV8ZJYdAsRIzrSobepxQZpI0ALei32fGoUpT94lAxdhGFoY4dQbrexAyV3lwb6u2yM2oTbwp7clyrNEz00Gc2vkxHJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)