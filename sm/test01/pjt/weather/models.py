from django.db import models

# Create your models here.
from django.db import models

class Weather(models.Model):
    dt_txt = models.DateTimeField()
    temp = models.FloatField()
    feels_like = models.FloatField()
    