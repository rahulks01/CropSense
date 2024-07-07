from django.core.management.base import BaseCommand
from ...weather_service import fetch_weather_data

class Command(BaseCommand):
    help = 'Fetches weather data for a given location'

    def add_arguments(self, parser):
        parser.add_argument('location', type=str, help='Location to fetch weather for')

    def handle(self, *args, **kwargs):
        location = kwargs['location']
        try:
            weather = fetch_weather_data(location)
            self.stdout.write(self.style.SUCCESS(f'Successfully fetched weather for {location}'))
        except ValueError as e:
            self.stderr.write(self.style.ERROR(f'Error: {str(e)}'))
