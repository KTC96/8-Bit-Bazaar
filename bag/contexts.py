from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from django.shortcuts import get_object_or_404
from games.models import Game

def bag_contents(request):
    bag_items = []
    total = 0
    game_count = 0
    bag = request.session.get('bag', {})
    free_game_delta = 0

    for item_id, quantity in bag.items():
        game = get_object_or_404(Game, pk=item_id)

        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            discounted_price = round(game.price - (game.price * sale_amount), 2)
            total += round(quantity * discounted_price, 2)
        else:
            discounted_price = 0 
            total += round(quantity * game.price, 2)

        game_count += quantity

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'game': game,
            'discounted_price': discounted_price,
        })

    if total < settings.FREE_GAME_THRESHOLD:
        free_game_delta = round(settings.FREE_GAME_THRESHOLD - total, 2)

    context = {
        'bag_items': bag_items,
        'total': round(total, 2),
        'game_count': game_count,
        'free_game_delta': free_game_delta,
        'free_game_threshold': round(settings.FREE_GAME_THRESHOLD, 2),
    }

    return context
