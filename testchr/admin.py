from django.contrib import admin
from testchr.models import Station, Project
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Station)
class Station_testAdmin(admin.ModelAdmin):
    list_display = ['station_id', 'name', 'empty_slots', 'free_bikes', 'latitude', 'longitude']
    

class ProjectResource(resources.ModelResource):
   class Meta:
      model = Project
class ProjectAdmin(ImportExportModelAdmin):
   resource_class = ProjectResource
   list_display = ['no', 'nombre', 'enlace', 'tipo', 'region', 'tipologia', 'titular', 'inversion', 'fechaPresentacionFecha_de_Ingreso', 'estado', 'mapa']


admin.site.register(Project,ProjectAdmin)