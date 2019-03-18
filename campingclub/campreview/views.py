from django.shortcuts import render, get_object_or_404
from.models import Campground, Campsite, CampsiteFeatures, Features
from .forms import CampForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'campreview/index.html')

def campground(request):
    campground=Campground.objects.all()
    return render(request, 'campreview/campground.html', {'campground': campground})


#form view
def addCampground(request):
    form=CampForm
    if request.method=='POST':
        form=CampForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=CampForm
    else:
        form=CampForm()
    return render (request, 'campreview/addcampground.html', {'form': form})


