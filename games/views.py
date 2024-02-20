from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Game, Category, Genre, Review
from .forms import GameForm, ReviewForm



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
    reviews = Review.objects.filter(game=game)

    if game.on_sale:
        sale_amount = Decimal(settings.SALE_AMOUNT)
        discounted_price = round(game.price - (game.price * sale_amount), 2)
    else:
        discounted_price = None

    context = {
        'game': game,
        'discounted_price': discounted_price,
        'reviews': reviews,
    }
    return render(request, 'games/game_detail.html', context)

@login_required
def add_game(request):
    """ Add a game to the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that action is for the 8BitBazaar team only!')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, 'Successfully added game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed to add game. Please ensure the form is valid.')
    else:
        form = GameForm()

    template = 'games/add_game.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_game(request, game_id):
    """ Edit a game in the shop """ 
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that action is for the 8BitBazaar team only!')
        return redirect(reverse('home'))

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed to update game. Please ensure the form is valid.')
    else:
        form = GameForm(instance=game)
        messages.info(request, f'You are editing {game.friendly_name}')

    template = 'games/edit_game.html'
    context = {
        'form': form,
        'game': game,
    }

    return render(request, template, context)

@login_required
def delete_game(request, game_id):
    """ Delete a game from the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, that action is for the 8BitBazaar team only!')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game deleted!')
    return redirect(reverse('games'))

@login_required
def review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_profile = request.user.userprofile

    # Check if user has made any orders
    if not user_profile.orders.exists():
        messages.error(request, "To leave a review on a game, you must purchase it first")
        return redirect('game_detail', game_id)

    # Check if user has purchased the specific game
    if not any(item.game == game for order in user_profile.orders.all() for item in order.line_items.all()):
        messages.error(request, "You must have purchased this game to review it.")
        return redirect('game_detail', game_id)

   # Check if the user has already reviewed the game
    if Review.objects.filter(game=game, author=request.user).exists():
        messages.error(request, "You have already reviewed this game. Please update or delete your existing review.")
        return redirect('game_detail', game_id)

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()

            messages.success(request, "Your review has been added.")
            return redirect('game_detail', game_id)

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'review.html', context)