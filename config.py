import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')  # Get from OpenWeatherMap
    CORS_HEADERS = 'Content-Type'