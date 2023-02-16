from django.urls import path

from . import views

urlpatterns = [
    path('', views.save_stations_data, name='save_stations_data'),
    path('data', views.display_stations_data, name='display_stations_data'),
]