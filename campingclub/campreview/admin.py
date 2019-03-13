from django.contrib import admin
from .models import Campground, Campsite, CampsiteFeatures, Features

# Register your models here.

admin.site.register(Campground)
admin.site.register(Features)
admin.site.register(CampsiteFeatures)
admin.site.register(Campsite)