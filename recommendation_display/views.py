from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_index(request):
    return HttpResponse("you found it! Well done.")

def recommendation_display_view(request):
    """Display a user's recommendations."""
    return render(request, "recommendation_display/base.html", context=None)
