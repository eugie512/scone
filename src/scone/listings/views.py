# Create your views here.
from listings.models import Listing
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_listings = Listing.objects.all().order_by('-list_date')[:5]
    return render_to_response('listings/index.html', {'latest_listings': latest_listings,})

def details(request, list_id):
    p = get_object_or_404(Listing, pk=list_id)
    return render_to_response('listings/detail.html', {'listing': p})