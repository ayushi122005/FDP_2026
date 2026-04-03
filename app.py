from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from config import Config
import os

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = Config.WEATHER_API_KEY or os.getenv('WEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5"

@app.route('/')
def home():
    return jsonify({
        "message": "Weather Forecast API",
        "status": "running",
        "endpoints": {
            "current": "/weather/current?city=<city>&country=<country>",
            "forecast": "/weather/forecast?city=<city>&country=<country>",
            "search": "/weather/search?q=<query>"
        }
    })

@app.route('/weather/current')
def get_current_weather():
    city = request.args.get('city')
    country = request.args.get('country', 'US')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    url = f"{BASE_URL}/weather"
    params = {
        'q': f"{city},{country}",
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_data = {
            "city": data['name'],
            "country": data['sys']['country'],
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "description": data['weather'][0]['description'].capitalize(),
            "icon": data['weather'][0]['icon'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "wind_speed": data['wind']['speed'],
            "visibility": data.get('visibility', 0) / 1000 if data.get('visibility') else 0,
            "timestamp": data['dt']
        }
        
        return jsonify(weather_data)
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Weather data not found", "details": str(e)}), 404
    except KeyError:
        return jsonify({"error": "Invalid city or country"}), 404

@app.route('/weather/forecast')
def get_weather_forecast():
    city = request.args.get('city')
    country = request.args.get('country', 'US')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    url = f"{BASE_URL}/forecast"
    params = {
        'q': f"{city},{country}",
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        forecast_list = []
        for item in data['list'][:8]:  # Next 8 three-hour periods (24 hours)
            forecast = {
                "time": item['dt_txt'],
                "temperature": item['main']['temp'],
                "description": item['weather'][0]['description'].capitalize(),
                "icon": item['weather'][0]['icon'],
                "humidity": item['main']['humidity']
            }
            forecast_list.append(forecast)
        
        return jsonify({
            "city": data['city']['name'],
            "country": data['city']['country'],
            "forecast": forecast_list
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Forecast data not found", "details": str(e)}), 404

@app.route('/weather/search')
def search_cities():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Search query is required"}), 400
    
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': query,
        'limit': 5,
        'appid': WEATHER_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        cities = response.json()
        
        city_list = [{
            "name": city['name'],
            "country": city['country'],
            "lat": city['lat'],
            "lon": city['lon']
        } for city in cities]
        
        return jsonify(city_list)
        
    except requests.exceptions.RequestException:
        return jsonify({"error": "Search failed"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)