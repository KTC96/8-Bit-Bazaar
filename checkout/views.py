import json
from decimal import Decimal
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)

from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from games.models import Game
from bag.contexts import bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .forms import OrderForm
from .models import Order, OrderLineItem, Discount, AppliedDiscount


import stripe
from django.utils import timezone
from django.db import transaction


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Check if discount code is submitted
    if request.method == 'POST' and 'discount_code' in request.POST:
        discount_code = request.POST['discount_code']
        try:
            discount = Discount.objects.get(
                code=discount_code, start_date__lte=timezone.now(),
                end_date__gte=timezone.now())

            # Check if the discount is valid and applicable
            is_new_user = (
                request.user.is_authenticated and
                request.user.date_joined.date() == timezone.now().date()
            )

            if discount.is_valid(is_new_user):
                # Apply discount logic here
                bag = request.session.get('bag', {})

                # Check if discounted total is available in session
                discounted_total = request.session.get(
                    'discounted_total', None)
                if discounted_total is None:
                    # Calculate total and apply discount
                    # if not available in session
                    current_bag = bag_contents(request)
                    total = current_bag['total']
                    discounted_total = total - (total * discount.amount)
                    # Store the discounted total in the session
                    request.session['discounted_total'] = discounted_total

                messages.success(
                    request,
                    f'Discount "{discount_code}" applied successfully!')
            else:
                messages.error(
                    request,
                    (
                        f'Discount code "{discount_code}" '
                        f'is not valid for your user type.'
                    )
                )
        except Discount.DoesNotExist:
            messages.error(request, f'Invalid discount code "{discount_code}"')

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    game = Game.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Game.DoesNotExist:
                    messages.error(
                        request,
                        f"The game with ID {item_id} "
                        f"in your bag wasn't found in our database."
                    )
                    continue

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request,
                'There was an error with your form. '
                'Please double-check your information.'
            )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('games'))

        current_bag = bag_contents(request)
        total = 0

        for item in current_bag['bag_items']:
            # Check if the game is already discounted
            discounted_price = (
                item['discounted_price']
                if item['discounted_price']
                else item['game'].price
            )
            total += round(item['quantity'] * discounted_price, 2)

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'discounted_total': request.GET.get('discounted_total'),
        'discount_amount': request.GET.get('discount_amount'),
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    order_games = Game.objects.filter(orderlineitem__order=order)

    for game in order_games:
        if game.on_sale:
            sale_amount = Decimal(settings.SALE_AMOUNT)
            game.discounted_price = round(game.price - (
                game.price * sale_amount), 2)
        else:
            game.discounted_price = None

    # Check if discounted total and discount amount are available in session
    discounted_total = request.session.get('discounted_total', None)
    discount_amount = request.session.get('discount_amount', None)

    if discounted_total:
        order.discounted_total = discounted_total
        order.save()

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f"Great news! We've processed your order! \
        Your order number is {order_number}. Keep an eye on your email \
        at {order.email} for a confirmation message.")

    request.session.pop('bag', None)
    request.session.pop('discounted_total', None)
    request.session.pop('discount_amount', None)

    discount_amount = request.session.get('discount_amount', None)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'discount_amount': discount_amount,
        'order_games': order_games,
    }

    order.discounted_total = discounted_total
    order.save()

    _send_confirmation_email(order)

    return render(request, template, context)


def apply_discount(request):
    """ Apply the discount code """
    
    if request.method == 'POST':
        discount_code = request.POST.get('discount_code')

        # Check if discount code is empty or None
        if not discount_code:
            messages.warning(
                request,
                'No discount code entered. '
                'Please enter a valid discount code.'
            )
            return redirect('checkout')

        try:
            discount = Discount.objects.get(code=discount_code)

            if request.user.is_authenticated:
                # Check if the discount has already been applied
                applied_discount_exists = AppliedDiscount.objects.filter(
                    user=request.user, discount=discount).exists()

                if not applied_discount_exists:
                    bag = request.session.get('bag', {})

                    # Calculate total directly
                    total_before_discount = sum(
                        float(item_data['discounted_price'])
                        if 'discounted_price' in item_data
                        else float(item_data['game'].price)
                        for item_data in bag_contents(request)['bag_items']
                    )

                    discount_amount = (
                        total_before_discount * discount.percentage / 100)
                    discounted_total = total_before_discount - discount_amount

                    # Apply the discount
                    AppliedDiscount.objects.create(
                        user=request.user, discount=discount)

                    # Convert Decimal values to float for serialization
                    request.session['discounted_total'] = float(
                        discounted_total)
                    request.session['discount_amount'] = float(discount_amount)
                    messages.success(
                        request,
                        f'Discount "{discount_code}" applied successfully!')
                else:
                    messages.info(
                        request,
                        'This discount code has already been applied.')
            else:
                messages.warning(
                    request,
                    'You need to be logged in to apply a discount.'
                    'Please log in or create an account.')
        except Discount.DoesNotExist:
            messages.error(request, f'Invalid discount code "{discount_code}"')

    # Redirect back to the checkout page
    return redirect('checkout')

    # Redirect back to the checkout page
    return redirect('checkout')


def _send_confirmation_email(order):
    """Send the user a confirmation email"""
    if not order.email_sent:  # Check if email has already been sent
        cust_email = order.email

        # Specify the path to the text file containing the email subject
        subject_file_path = (
            'checkout/templates/checkout/confirmation_emails/'
            'confirmation_email_subject.txt'
        )
        body_file_path = (
            'checkout/templates/checkout/confirmation_emails/'
            'confirmation_email_body.txt'
        )

        # Read the content of the text files
        with open(subject_file_path, 'r') as subject_file:
            subject = subject_file.read()

        subject = subject.replace(
            '{{ order.order_number }}', str(order.order_number))

        with open(body_file_path, 'r') as body_file:
            body = body_file.read()

        # Initialize free_game_link
        free_game_link = ''

        # Check if the free game threshold is met
        if (
            (order.discounted_total is not None and
             order.discounted_total >= settings.FREE_GAME_THRESHOLD) or
            (order.total is not None and
             order.total >= settings.FREE_GAME_THRESHOLD)
        ):
            free_game_link = 'https://stephendawsondev.github.io/j-day/'
            print(f"Debugging: free_game_link is set to {free_game_link}")
            body += f"\nEnjoy your free game! {free_game_link}"

        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'free_game_link': free_game_link
            }

        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

        order.email_sent = True
        order.save()