from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecommendationForm
from .utils import get_labeled_profile_picture, get_new_labeled_pictures

# Create your views here.

def test_index(request):
    return HttpResponse("you found it! Well done.")

def index_view(request):
    return render(request, "base_generic.html")

def recommendation_display_view(request):
    """Display a user's recommendations."""
    load_new = False
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['new']:
                load_new = True
    else:
        form = RecommendationForm()

    #grab a new profile picture
    if load_new:
        get_new_labeled_pictures()

    newpic = get_labeled_profile_picture()
    context = {'form': form, 
                'picture': newpic}
    return render(request, "recommendation_display/rec_display.html", context=context)

    
