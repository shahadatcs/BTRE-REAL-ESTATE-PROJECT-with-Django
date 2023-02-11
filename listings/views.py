from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Listing


# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)
    contex = {
        'listings':page_listings
    }
    return render(request, 'listings/listings.html',contex)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')