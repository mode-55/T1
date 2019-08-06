from django.db import models
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):


  title = models.CharField(max_length=256, null=True, blank=True)
  completed = models.BooleanField(blank=True, default=False)
  url = models.CharField(max_length=256, null=True, blank=True)
  order = models.IntegerField(null=True, blank=True)
  
  #User location 
  location_accuracy_radius = models.IntegerField(null=True, blank=True)
  location_latitude = models.FloatField(blank=False, null=False,default=0.0)
  location_longitude = models.FloatField(blank=False, null=False,default=0.0)
  location_metro_code = models.IntegerField(null=True, blank=True)
  location_time_zone = models.CharField(max_length=256, null=True, blank=True)
  ip_address = models.CharField(max_length=64, verbose_name="ipaddress",
                 default="", unique=False, null=True, blank=True)
  city = models.CharField(max_length=256, null=True, blank=True)
  country_iso_code = models.CharField(max_length=20, null=True, blank=True)
  country_name =  models.CharField(max_length=256, null=True, blank=True)
  createdon = models.DateTimeField(default=timezone.now) 

