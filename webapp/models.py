from django.db import models

# Create your models here.
class Record(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    crop_name = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    harvest_time = models.CharField(max_length=50)
    quantity = models.IntegerField(default=5)
    price = models.IntegerField(default=30)

    def __str__(self) :
        return(f"{self.crop_name}")
