from celery import Celery
import requests
from .models import WeatherData

app = Celery('weather',broker='redis://localhost:6379/0')

@app.task
def fetch_weather(location, api_key):
    WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': location,  # Example: 'Nairobi,KE'
        'appid': api_key, 
    }

    response = requests.get(WEATHER_API_URL, params=params)
  
    if response.status_code == 200:
        weather_data =  response.json() 
        WeatherData.objects.create(
            location=location,
            temperature=weather_data['main']['temp'],
            humidity=weather_data['main']['humidity'],
            conditions=weather_data['weather'][0]['description']
        )
        print(weather_data)
        return weather_data
    
    else:
        return {'error' : 'Unable to fetch weather data'}
    