from decimal import Decimal
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponse
)
from django.contrib.auth.decorators import login_required
from games.models import Game
from .models import Wishlist
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from bag.contexts import bag_contents


@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    games_in_wishlist = wishlist.games.all()

    for game in games_in_wishlist:
        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            game.discounted_price = round(
                game.price - (game.price * sale_amount), 2)
        else:
            game.discounted_price = None

    return render(
        request,
        'wishlist/wishlist.html', {'games_in_wishlist': games_in_wishlist})


@login_required
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if game not in wishlist.games.all():

        wishlist.games.add(
            game, through_defaults={'date_added': timezone.now()})
        messages.success(
            request, f'Added {game.friendly_name} to your wishlist')
    else:
        messages.info(
            request, f'{game.friendly_name} is already in your wishlist')

    return redirect(reverse('game_detail', args=[game_id]))


@login_required
def remove_from_wishlist(request, game_id):
    """Remove the game from the wishlist"""

    game = get_object_or_404(Game, pk=game_id)

    try:
        wishlist = Wishlist.objects.get(user=request.user)

        # Check if the game is in the wishlist
        if game in wishlist.games.all():
            # Remove the game from the wishlist
            wishlist.games.remove(game)

            messages.success(
                request, f'Removed {game.friendly_name} from your wishlist')
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    except Wishlist.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_to_bag_wishlist(request, game_id):
    """ Add a quantity of the game to the shopping bag """

    game = get_object_or_404(Game, pk=game_id)

    quantity = 1

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    game_id_str = str(game_id)

    if game_id_str in bag:
        bag[game_id_str] += quantity
        messages.success(request, f'Added {game.friendly_name} to your bag')
    else:
        bag[game_id_str] = quantity
        messages.success(request, f'Added {game.friendly_name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
