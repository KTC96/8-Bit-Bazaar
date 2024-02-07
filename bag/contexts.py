from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    game_count = 0

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