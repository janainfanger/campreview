from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('campground/', views.campground, name='campground'),
    path('campsites/<int:id>', views.campsites, name='campsite'), #the int id part includes the id in the url
    path('addCampground/', views.addCampground, name='addcampground'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]