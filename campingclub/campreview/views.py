from django.shortcuts import render, get_object_or_404
from.models import Campground, Campsite, CampsiteFeatures, Features

# Create your views here.

def index(request):
    return render(request, 'campreview/index.html')

def campground(request):
    campground=Campground.objects.all()
    return render(request, 'campreview/campground.html', {'campground': campground})


    