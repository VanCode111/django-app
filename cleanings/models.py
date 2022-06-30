from django.db import models
from simple_history.models import HistoricalRecords

class Cleaning(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    completed = models.BooleanField(default=False)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='city')
    history = HistoricalRecords()

class City(models.Model):
    name = models.CharField(max_length=100)
