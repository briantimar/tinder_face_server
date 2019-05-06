from django import forms

class RecommendationForm(forms.Form):
    """ Form which lets user interact with recommendations """
    # check to like the current profile
    like = forms.BooleanField(required=False)
    