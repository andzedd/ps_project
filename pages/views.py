from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-id').filter(is_published=True)[:6]

    context = {
        'listings': listings
    }
    return render(request, 'index.html', context)

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
