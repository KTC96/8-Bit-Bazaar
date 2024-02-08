from django.shortcuts import render, redirect, get_object_or_404
from games.models import Game
from decimal import Decimal
from django.conf import settings

def view_bag(request):
    """ Returns the bag contents page"""

    games = Game.objects.all()
    for game in games:
            if game.on_sale:
                sale_amount = Decimal(settings.SALE_AMOUNT)
                discounted_price = round(game.price - (game.price * sale_amount), 2)
            else:
                discounted_price = None


    context = {
            'discounted_price': discounted_price,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the game to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        

    request.session['bag'] = bag
    return redirect(redirect_url)
    