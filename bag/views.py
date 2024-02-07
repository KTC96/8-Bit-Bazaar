from django.shortcuts import render

def view_bag(request):
    """ Returns the bag contents page"""
    return render(request, 'bag/bag.html')
