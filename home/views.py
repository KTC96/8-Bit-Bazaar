from django.shortcuts import render

def index(request):
    """ Returns the index page """
    return render(request, 'home/index.html')

def privacy_policy(request):
    """ Returns the privacy policy page """
    return render(request, 'home/privacy_policy.html')

