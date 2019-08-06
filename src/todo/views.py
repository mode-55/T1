from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response
import requests, json, random
from retrying import retry
from ipify import get_ip
from ipify.exceptions import IpifyException

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
  queryset = TodoItem.objects.all()
  serializer_class = TodoItemSerializer
  ip = ""

  #wait 1 to 2 seconds between retries and stop after 5 retries 
  @retry(wait_random_min=1000, wait_random_max=2000,stop_max_attempt_number=5)
  def request_location(self): 
    

    api_url = "http://api:8080/info?ip=" + self.ip
    
    try:
      r_ip = requests.get(api_url)  
      if(r_ip.status_code == 429):
        raise IOError("Rate limit responses (HTTP 429)")
      if(r_ip.status_code == 400):
        raise IOError("Bad request response (HTTP 400)")
      if(r_ip.status_code == 200):
        geoip_call = json.loads(r_ip.text)
        return geoip_call
    except requests.ConnectionError:
      # handle the exception
      print("Failed to connect to API")
    return False

  @retry(stop_max_attempt_number=5)
  def get_user_ip_address(self):
    try:
      ip = get_ip()
      return ip
    except:
      raise IOError("Couldn't get user IP from Ipify!")
    return ""


  def perform_create(self, serializer):
    # Save instance to get primary key and then update URL and location data 
    instance = serializer.save()
    ip = self.get_user_ip_address()
    instance.ip_address = ip
    geoip_call = self.request_location()
    if(geoip_call):
      instance.city = geoip_call.get('city')
      instance.country_iso_code = geoip_call.get('country').get('iso_code')
      instance.country_name = geoip_call.get('country').get('name')
      instance.location_accuracy_radius = geoip_call.get('location').get('accuracy_radius')
      instance.location_latitude = geoip_call.get('location').get('latitude')
      instance.location_longitude = geoip_call.get('location').get('longitude')
      instance.location_metro_code = geoip_call.get('location').get('metro_code')
      instance.location_time_zone = geoip_call.get('location').get('time_zone') 
    
    instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)

    #save record
    instance.save()

  # Deletes all todo items
  def delete(self, request):
    TodoItem.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 