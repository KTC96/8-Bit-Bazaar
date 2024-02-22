from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from games.models import Game
from django.contrib import messages
from django.conf import settings

def view_wishlist(request):
    """ Returns the wishlist contents page"""

    games = Game.objects.all()
    wishlist_items = request.session.get('wishlist', {}).items()
    for game in games:
        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            discounted_price = round(game.price - (game.price * sale_amount), 2)
        else:
            discounted_price = None
    
    context = {
            'discounted_price': discounted_price,
            'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, item_id):
    """ Add a game to the shopping wishlist """
    
    game = get_object_or_404(Game, pk=item_id)
    
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in wishlist:
        messages.success(request, f'{game.friendly_name} is already in your wishlist')
    else:
        wishlist[item_id] = 1
        messages.success(request, f'Added {game.friendly_name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

def remove_from_wishlist(request, item_id):
    """Remove the game from the wishlist"""

    game = get_object_or_404(Game, pk=item_id)

    try:
        wishlist = request.session.get('wishlist', {})

        if item_id in wishlist:
            wishlist.pop(item_id)
            request.session['wishlist'] = wishlist
            messages.success(request, f'Removed {game.friendly_name} from your wishlist')
            return HttpResponse(status=200)
            
        else:
            return HttpResponse(status=404) 
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
