from django.db import models

# Create your models here.
class Record(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    crop_name = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    harvest_time = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50, default=5)
    price = models.CharField(max_length=10, default=30)
    ideal_temperature_min = models.FloatField(default=20)
    ideal_temperature_max = models.FloatField(default=35)
    ideal_humidity_min = models.FloatField(default=35)
    ideal_humidity_max = models.FloatField(default=70)
    ideal_rainfall_min = models.FloatField(default=300)
    ideal_rainfall_max = models.FloatField(default=800)

    def __str__(self):
        return self.name

class Weather(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.date}"