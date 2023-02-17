from django.urls import path

from . import views

urlpatterns = [
    path('', views.save_stations_data, name='save_stations_data'),
    path('stations', views.display_stations_data, name='display_stations_data'),
    path('projects', views.display_projects_data, name='display_projects_data'),
]