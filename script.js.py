const API_BASE = 'http://localhost:5000'; // Change to your backend URL in production
const ICON_BASE_URL = 'https://openweathermap.org/img/wn/';

class WeatherApp {
    constructor() {
        this.cityInput = document.getElementById('cityInput');
        this.searchBtn = document.getElementById('searchBtn');
        this.suggestions = document.getElementById('searchSuggestions');
        
        this.initEventListeners();
    }

    initEventListeners() {
        this.searchBtn.addEventListener('click', () => this.searchWeather());
        this.cityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.searchWeather();
        });
        this.cityInput.addEventListener('input', (e) => this.searchCities(e.target.value));
        
        // Click outside to close suggestions
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-section')) {
                this.suggestions.classList.add('hidden');
            }
        });
    }

    async searchCities(query) {
        if (query.length < 2) {
            this.suggestions.classList.add('hidden');
            return;
        }

        try {
            const response = await fetch(`${API_BASE}/weather/search?q=${encodeURIComponent(query)}`);
            const cities = await response.json();
            
            this.showSuggestions(cities);
        } catch (error) {
            console.error('Search error:', error);
        }
    }

    showSuggestions(cities) {
        this.suggestions.innerHTML = '';
        
        if (cities.length === 0) {
            this.suggestions.classList.add('hidden');
            return;
        }

        cities.forEach((city, index) => {
            const suggestion = document.createElement('div');
            suggestion.className = 'suggestion-item';
            suggestion.innerHTML = `
                <strong>${city.name}, ${city.country}</strong>
                <small>${city.lat.toFixed(2)}°N, ${city.lon.toFixed(2)}°E</small>
            `;
            suggestion.addEventListener('click', () => this.selectCity(city));
            suggestion.addEventListener('mouseenter', () => suggestion.classList.add('active'));
            suggestion.addEventListener('mouseleave', () => suggestion.classList.remove('active'));
            this.suggestions.appendChild(suggestion);
        });

        this.suggestions.classList.remove('hidden');
    }

    selectCity(city) {
        this.cityInput.value = `${city.name}, ${city.country}`;
        this.suggestions.classList.add('hidden');
        this.searchWeather();
    }

    async searchWeather() {
        const query = this.cityInput.value.trim();
        if (!query) return;

        this.showLoading();
        this.hideError();

        try {
            const [currentRes, forecastRes] = await Promise.all([
                fetch(`${API_BASE}/weather/current?city=${encodeURIComponent(query)}`),
                fetch(`${API_BASE}/weather/forecast?city=${encodeURIComponent(query)}`)
            ]);

            if (!currentRes.ok || !forecastRes.ok) {
                throw new Error('Weather data not found');
            }

            const currentData = await currentRes.json();
            const forecastData = await forecastRes.json();

            this.displayCurrentWeather(currentData);
            this.displayForecast(forecastData);
            
        } catch (error) {
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    displayCurrentWeather(data) {
        document.getElementById('currentCity').textContent = `${data.city}, ${data.country}`;
        document.getElementById('currentTemp').textContent = Math.round(data.temperature);
        document.getElementById('currentDescription').textContent = data.description;
        document.getElementById('currentIcon').src = `${ICON_BASE_URL}${data.icon}@2x.png`;
        document.getElementById('humidity').innerHTML = `<i class="fas fa-tint"></i> ${data.humidity}%`;
        document.getElementById('windSpeed').innerHTML = `<i class="fas fa-wind"></i> ${data.wind_speed} m/s`;
        document.getElementById('visibility').innerHTML = `<i class="fas fa-eye"></i> ${data.visibility} km`;

        document.getElementById('currentWeather').classList.remove('hidden');
        document.getElementById('forecastSection').classList.remove('hidden');
    }

   