from decimal import Decimal
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponse
)

from games.models import Game
from django.contrib import messages
from django.conf import settings


def view_bag(request):
    """ Returns the bag contents page"""

    games = Game.objects.all()
    for game in games:
        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            discounted_price = round(game.price - (
                game.price * sale_amount), 2)
        else:
            discounted_price = None

    context = {
            'discounted_price': discounted_price,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the game to the shopping bag """

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.add_message(
            request, messages.SUCCESS,
            f'Added {game.friendly_name} to your bag')
    else:
        bag[item_id] = quantity
        messages.add_message(
            request, messages.SUCCESS,
            f'Added {game.friendly_name} to your bag')

    request.session['bag'] = bag

    request.session['item_added_to_bag'] = True

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of games"""

    game = get_object_or_404(Game, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {game.friendly_name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Removed {game.friendly_name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the game from the bag"""

    game = get_object_or_404(Game, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            request.session['bag'] = bag
            messages.success(
                request, f'Removed {game.friendly_name} from your bag')
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
