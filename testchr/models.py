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
