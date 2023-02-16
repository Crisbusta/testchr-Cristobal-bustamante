from django.contrib import admin
from testchr.models import Station

# Register your models here.
@admin.register(Station)
class Station_testAdmin(admin.ModelAdmin):
    list_display = ['station_id', 'name', 'empty_slots', 'free_bikes', 'latitude', 'longitude']