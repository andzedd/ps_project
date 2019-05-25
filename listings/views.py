from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def index(request):
    listings = Listing.objects.all().filter(is_published=True)

    paginator = Paginator(listings,10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/index.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-id')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords) | Q(category__icontains=keywords))

    context = {
        'listings': queryset_list
    }
    
    return render(request, 'listings/search.html', context)

    # listings = Listing.objects.all().filter(category='Hardware')
    # paginator = Paginator(listings,10)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    # context = {
    #     'listings': paged_listings
    # }
    # return render(request, 'listings/search.html', context)