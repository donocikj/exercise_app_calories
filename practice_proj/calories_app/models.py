from django.db import models
from django.utils import timezone

# Create your models here.

class Meal(models.Model):
    """ representation of a meal registered to certain date and with a given amount of calories """
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    date = models.DateField(default=timezone.now)
