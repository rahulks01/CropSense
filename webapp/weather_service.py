# weather_service.py
import requests
from django.utils import timezone
from .models import Weather

API_KEY = '74840cc2110c573f8bd84cfc2aee64b9'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric' 
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # print(f"DEBUG: API Response - {data}")  # Debug print to inspect API response

    if response.status_code == 200:
        temperature = data['main']['temp'] if 'main' in data and 'temp' in data['main'] else None
        humidity = data['main']['humidity'] if 'main' in data and 'humidity' in data['main'] else None
        rainfall = data.get('rain', {}).get('1h', 0)
        
        if temperature is not None and humidity is not None:
            weather = Weather(
                location=location,
                temperature=temperature,
                humidity=humidity,
                rainfall=rainfall,
                date=timezone.now()
            )
            weather.save()
            # print(f"DEBUG: Saved Weather Data - {weather}") 
            return weather
        else:
            raise ValueError("Incomplete data received from API.")
    
    elif response.status_code == 404:
        raise ValueError("Location not found.")
    elif response.status_code == 401:
        raise ValueError("Invalid API key.")
    else:
        raise ValueError(f"Error fetching data: {data.get('message', 'Unknown error')}")
