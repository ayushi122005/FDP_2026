<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Forecast App</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-cloud-sun"></i> Weather Forecast</h1>
            <p>Get real-time weather updates for any location</p>
        </header>

        <div class="search-section">
            <div class="search-box">
                <input type="text" id="cityInput" placeholder="Enter city name (e.g., London, UK)">
                <button id="searchBtn"><i class="fas fa-search"></i></button>
            </div>
            <div id="searchSuggestions" class="suggestions"></div>
        </div>

        <div id="currentWeather" class="weather-card current-weather hidden">
            <div class="weather-header">
                <h2 id="currentCity"></h2>
                <div class="temp-container">
                    <span id="currentTemp" class="current-temp"></span>
                    <span class="temp-unit">°C</span>
                </div>
            </div>
            <div class="weather-body">
                <div class="weather-icon">
                    <img id="currentIcon" src="" alt="Weather icon">
                </div>
                <p id="currentDescription" class="description"></p>
                <div class="weather-details">
                    <div class="detail-item">
                        <i class="fas fa-tint"></i>
                        <span id="humidity"></span>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-wind"></i>
                        <span id="windSpeed"></span>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-eye"></i>
                        <span id="visibility"></span>
                    </div>
                </div>
            </div>
        </div>

        <div id="forecastSection" class="forecast-section hidden">
            <h3>24-Hour Forecast</h3>
            <div id="forecastList" class="forecast-grid"></div>
        </div>

        <div id="errorMessage" class="error-message hidden"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>