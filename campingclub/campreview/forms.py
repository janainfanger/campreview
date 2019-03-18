from django import forms
from .models import Campground, Campsite, CampsiteFeatures

class CampForm(forms.ModelForm):
    class Meta:
        model=Campground
        fields='__all__'