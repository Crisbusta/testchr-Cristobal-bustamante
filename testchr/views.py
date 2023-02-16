from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Station
import requests

# Create your views here.

def save_stations_data(request):
    response = requests.get(url="http://api.citybik.es/v2/networks/bikesantiago")
    response.raise_for_status()
    data = response.json()
    for station_data in data['network']['stations']:
        Station.objects.create(
            empty_slots=station_data['empty_slots'],
            free_bikes=station_data['free_bikes'],
            station_id=station_data['id'],
            latitude=station_data['latitude'],
            longitude=station_data['longitude'],
            name=station_data['name']
        )
    return JsonResponse({"status": "success"})

def display_stations_data(request):
    template_name = 'stations_data.html'
    stations = Station.objects.all()[:10]
    args = {'stations':stations}
    return render(request, template_name, args)
