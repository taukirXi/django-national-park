from django import forms
from .models import TravelEntries

class AddPost(forms.ModelForm):
    class Meta:
        model = TravelEntries
        fields = ['author_name', 'place_name', 'text']
       