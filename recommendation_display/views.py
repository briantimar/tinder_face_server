from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecommendationForm
from .utils import get_unlabeled_profile_picture

# Create your views here.

def test_index(request):
    return HttpResponse("you found it! Well done.")

def index_view(request):
    return render(request, "base_generic.html")

def recommendation_display_view(request):
    """Display a user's recommendations."""
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            print("Valid form!")

    else:
        form = RecommendationForm()
    #grab a new profile picture
    newpic = get_unlabeled_profile_picture()
    context = {'form': form, 
                'picture': newpic}
    return render(request, "recommendation_display/rec_display.html", context=context)

    
