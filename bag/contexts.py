from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Game


def bag_contents(request):

    bag_items = []
    total = 0
    game_count = 0
    bag = request.session.get('bag',{}) 

    for item_id, quantity in bag.items():
        game = get_object_or_404(Game, pk=item_id)
        total += quantity * game.price
        game_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity, 
            'game': game, 
        })
        


    if total < settings.FREE_GAME_THRESHOLD:
        free_game_delta = settings.FREE_GAME_THRESHOLD - total
    else:
        free_game_delta = 0
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'game_count': game_count,
        'free_game_delta': free_game_delta,
        'free_game_threshold': settings.FREE_GAME_THRESHOLD,
    }

    return context

    