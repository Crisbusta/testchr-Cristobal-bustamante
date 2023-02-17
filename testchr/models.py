from django.db import models
class Station(models.Model):
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    station_id = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Project(models.Model):
    no = models.IntegerField()
    nombre = models.CharField(max_length=2000)
    enlace = models.CharField(max_length=2000)
    tipo = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    tipologia = models.CharField(max_length=500)
    titular = models.CharField(max_length=2000)
    inversion = models.CharField(max_length=100)
    fechaPresentacionFecha_de_Ingreso = models.CharField(max_length=2000)
    estado = models.CharField(max_length=500)
    mapa = models.CharField(max_length=200)

