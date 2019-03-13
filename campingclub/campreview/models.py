from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Features(models.Model):
    featurename=models.CharField(max_length=255)

    def __str__(self):
        return self.featurename

    class Meta:
        db_table='Features'


class Campground(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    features=models.ManyToManyField(Features)
    description=models.TextField(max_length=255)
    
    def __str__(self):
        return self.name  

    class Meta:
        db_table='Campground'

class CampsiteFeatures(models.Model):
    viewtype=models.CharField(max_length=100)
    trees=models.CharField(max_length=100)
    partysize=models.IntegerField()
    privacy=models.CharField(max_length=50)
   
    def __str__(self):
        return self.viewtype

    class Meta:
        db_table='CampsiteFeatures'


class Campsite(models.Model):
    CampgroundID=models.ForeignKey(Campground, on_delete=models.DO_NOTHING)
    campsiteID=models.CharField(max_length=3)
    campsitefeatures=models.ManyToManyField(CampsiteFeatures)

    def __str__(self):
        return self.campsiteID

    class Meta:
        db_table='Campsite'


