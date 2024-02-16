from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.conf import settings
from .models import Game, Category, Genre
from .forms import GameForm

def all_games(request):
    """A view to show all games, including sorting and search queries"""
    
    games = Game.objects.all()
    query = None
    categories = None
    genres = None
    sort = None
    direction = None

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

    if 'genre' in request.GET:
        genres  = request.GET.getlist('genre')
        games = games.filter(genre__name__in=genres)
        genres = Genre.objects.filter(name__in=genres)

    for game in games:
        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            game.discounted_price = round(game.price - (game.price * sale_amount), 2)
        else:
            game.discounted_price = None

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('games'))
            
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
        'current_categories': categories,
        'current_genres': genres,
        'current_sorting': current_sorting,
    }

    return render(request, 'games/games.html', context)

def game_detail(request, game_id):
    """A view to show individual game details"""

    game = get_object_or_404(Game, pk=game_id)

    if game.on_sale:
        sale_amount = Decimal(settings.SALE_AMOUNT)
        discounted_price = round(game.price - (game.price * sale_amount), 2)
    else:
        discounted_price = None

    context = {
        'game': game,
        'discounted_price': discounted_price,
    }
    return render(request, 'games/game_detail.html', context)

def add_game(request):
    """ Add a game to the shop """
    form = GameForm()
    template = 'games/add_game.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
