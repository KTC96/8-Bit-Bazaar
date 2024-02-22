from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from games.models import Game
from .models import Wishlist
from django.contrib import messages
from django.conf import settings

@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    games_in_wishlist = wishlist.games.all()
    return render(request, 'wishlist/wishlist.html', {'games_in_wishlist': games_in_wishlist})

@login_required
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if game not in wishlist.games.all():
        wishlist.games.add(game)

    return redirect('wishlist')

@login_required
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
