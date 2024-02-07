from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Game, Category

def all_games(request):
    """A view to show all games, including sorting and search queries"""

    games = Game.objects.all()
    query = request.GET.get('q')
    categories = None
    sort = request.GET.get('sort')
    direction = request.GET.get('direction')

    if sort == 'name':
        sort_key = 'lower_name'
        games = games.annotate(lower_name=Lower('name')).order_by(f'{sort_key}{"" if direction!="desc" else "-"}')
    elif sort == 'category':
        sort_key = 'category__name'
        games = games.order_by(f'{sort_key}{"" if direction!="desc" else "-"}')

    if 'category' in request.GET:
        categories = request.GET.getlist('category')
        games = games.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        games = games.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    context = {
        'games': games,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'games/games.html', context)

def game_detail(request, game_id):
    """A view to show individual game details"""

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game_detail.html', context)
