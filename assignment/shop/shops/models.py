from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
