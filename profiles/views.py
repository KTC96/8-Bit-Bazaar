from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm



@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page' : True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    user_profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile)

    messages.info(request, (
        f'Hey, just a heads up about your previous order {order_number}. '
        'We sent a confirmation email on the day you placed it!'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'orders': orders,  # Pass the filtered orders to the template
        'from_profile': True,
    }

    return render(request, template, context)