from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_index(request):
    return HttpResponse("you found it! Well done.")

def index_view(request):
    return render(request, "base_generic.html")

def recommendation_display_view(request):
    """Display a user's recommendations."""
    return render(request, "recommendation_display/rec_display.html", context=None)

    
