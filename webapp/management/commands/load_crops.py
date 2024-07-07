from django.core.management.base import BaseCommand
from webapp.models import Record

class Command(BaseCommand):
    help = 'Load sample crop data'

    def handle(self, *args, **kwargs):
        crops_data = [
            {
                "crop_name": "Wheat",
                "season": "Rabi",
                "harvest_time": '4 months',
                "quantity": 2200,
                "price": 2200,
                "ideal_temperature_min": 10,
                "ideal_temperature_max": 25,
                "ideal_humidity_min": 40,
                "ideal_humidity_max": 70,
                "ideal_rainfall_min": 300,
                "ideal_rainfall_max": 500
            },
            {
                "crop_name": "Corn",
                "season": "Kharif",
                "harvest_time": '3 months',
                "quantity": 1800,
                "price": 1900,
                "ideal_temperature_min": 15,
                "ideal_temperature_max": 30,
                "ideal_humidity_min": 60,
                "ideal_humidity_max": 80,
                "ideal_rainfall_min": 500,
                "ideal_rainfall_max": 800
            },
            {
                "crop_name": "Rice",
                "season": "Kharif",
                "harvest_time": '4 months',
                "quantity": 2500,
                "price": 3200,
                "ideal_temperature_min": 20,
                "ideal_temperature_max": 35,
                "ideal_humidity_min": 70,
                "ideal_humidity_max": 90,
                "ideal_rainfall_min": 700,
                "ideal_rainfall_max": 1000
            },
            {
                "crop_name": "Soybean",
                "season": "Kharif",
                "harvest_time": '3 months',
                "quantity": 1600,
                "price": 3000,
                "ideal_temperature_min": 20,
                "ideal_temperature_max": 30,
                "ideal_humidity_min": 50,
                "ideal_humidity_max": 70,
                "ideal_rainfall_min": 450,
                "ideal_rainfall_max": 650
            },
            {
                "crop_name": "Barley",
                "season": "Rabi",
                "harvest_time": '4 months',
                "quantity": 1800,
                "price": 1700,
                "ideal_temperature_min": 8,
                "ideal_temperature_max": 22,
                "ideal_humidity_min": 30,
                "ideal_humidity_max": 60,
                "ideal_rainfall_min": 250,
                "ideal_rainfall_max": 450
            },
            {
                "crop_name": "Potato",
                "season": "Rabi",
                "harvest_time": '3 months',
                "quantity": 2200,
                "price": 800,
                "ideal_temperature_min": 10,
                "ideal_temperature_max": 20,
                "ideal_humidity_min": 60,
                "ideal_humidity_max": 85,
                "ideal_rainfall_min": 500,
                "ideal_rainfall_max": 700
            },
            {
                "crop_name": "Tomato",
                "season": "Kharif",
                "harvest_time": '2.5 months',
                "quantity": 2500,
                "price": 2000,
                "ideal_temperature_min": 18,
                "ideal_temperature_max": 28,
                "ideal_humidity_min": 50,
                "ideal_humidity_max": 75,
                "ideal_rainfall_min": 400,
                "ideal_rainfall_max": 600
            },
            {
                "crop_name": "Cotton",
                "season": "Kharif",
                "harvest_time": '5 months',
                "quantity": 1500,
                "price": 3500,
                "ideal_temperature_min": 25,
                "ideal_temperature_max": 35,
                "ideal_humidity_min": 40,
                "ideal_humidity_max": 60,
                "ideal_rainfall_min": 300,
                "ideal_rainfall_max": 500
            },
            {
                "crop_name": "Sugarcane",
                "season": "Perennial",
                "harvest_time": '12 months',
                "quantity": 70000,
                "price": 2800,
                "ideal_temperature_min": 20,
                "ideal_temperature_max": 35,
                "ideal_humidity_min": 60,
                "ideal_humidity_max": 80,
                "ideal_rainfall_min": 600,
                "ideal_rainfall_max": 900
            },
            {
                "crop_name": "Sunflower",
                "season": "Kharif",
                "harvest_time": '3.5 months',
                "quantity": 1000,
                "price": 4000,
                "ideal_temperature_min": 15,
                "ideal_temperature_max": 28,
                "ideal_humidity_min": 50,
                "ideal_humidity_max": 70,
                "ideal_rainfall_min": 400,
                "ideal_rainfall_max": 600
            }
        ]


        for crop_data in crops_data:
            Record.objects.create(**crop_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded crop data'))
