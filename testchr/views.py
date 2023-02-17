from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Station, Project
import requests
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

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
    default_page = 1
    page = request.GET.get('page', default_page)
    items_per_page = 10
    query = Station.objects.all()
    paginator = Paginator(query, items_per_page)
    try:
        stations = paginator.page(page)
    except PageNotAnInteger:
        stations = paginator.page(default_page)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)

    args = {'stations':stations}
    return render(request, template_name, args)

def display_projects_data(request):
    template_name = 'projects_data.html'
    default_page = 1
    page = request.GET.get('page', default_page)
    items_per_page = 10
    query = Project.objects.all().order_by('no').values()
    paginator = Paginator(query, items_per_page)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(default_page)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    args = {'projects':projects}
    return render(request, template_name, args)

