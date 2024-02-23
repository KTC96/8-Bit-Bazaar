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

def add_to_bag_wishlist(request, item_id):
    """ Add a quantity of the game to the shopping bag """

    game = get_object_or_404(Game, pk=item_id)
    
    # Check if quantity is provided in the request, default to 1 if not
    quantity = int(request.POST.get('quantity', 1))
    
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {game.friendly_name} to your bag')
        
    request.session['bag'] = bag
    return redirect(redirect_url)