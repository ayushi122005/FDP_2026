* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #74b9ff 0%, #0984e3 50%, #00b894 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

header p {
    font-size: 1.1rem;
    opacity: 0.9;
}

.search-section {
    margin-bottom: 30px;
}

.search-box {
    position: relative;
    max-width: 500px;
    margin: 0 auto 20px;
}

.search-box input {
    width: 100%;
    padding: 18px 50px 18px 20px;
    font-size: 1.1rem;
    border: none;
    border-radius: 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    outline: none;
    transition: all 0.3s ease;
}

.search-box input:focus {
    transform: translateY(-2px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

#searchBtn {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: #00b894;
    color: white;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}

#searchBtn:hover {
    background: #00a085;
    transform: translateY(-50%) scale(1.1);
}

.suggestions {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    max-height: 200px;
    overflow-y: auto;
    margin-top: 10px;
}

.suggestion-item {
    padding: 15px 20px;
    cursor: pointer;
    border-bottom: 1px solid #eee;
    transition: background 0.3s ease;
}

.suggestion-item:hover,
.suggestion-item.active {
    background: #f8f9fa;
}

.suggestion-item:last-child {
    border-bottom: none;
}

.weather-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-radius: 25px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
    transition: all 0.5s ease;
}

.weather-card.hidden {
    display: none;
}

.current-weather {
    text-align: center;
}

.weather-header h2 {
    font-size: 2rem;
    margin-bottom: 20px;
    color: #2d3436;
}

.temp-container {
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 10px;
}

.current-temp {
    font-size: 4rem;
    font-weight: 300;
    color: #00b894;
}

.temp-unit {
    font-size: 1.5rem;
    color: #636e72;
}

.weather-icon img {
    width: 120px;
    height: 120px;
    margin: 20px 0;
}

.description {
    font-size: 1.3rem;
    color: #2d3436;
    margin-bottom: 25px;
    text-transform: capitalize;
}

.weather-details {
    display: flex;
    justify-content: space-around;
    gap: 20px;
}

.detail-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #636e72;
}

.detail-item i {
    font-size: 1.5rem;
    margin-bottom: 5px;
    color: #00b894;
}

.forecast-section h3 {
    text-align: center;
    color: #2d3436;
    margin-bottom: 25px;
    font-size: 1.5rem;
}

.forecast-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 15px;
}

.forecast-item {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 15px;
    padding: 20px 10px;
    text-align: center;
    transition: transform 0.3s ease;
}

.forecast-item:hover {
    transform: translateY(-5px);
}

.forecast-icon {
    width: 50px;
    height: 50px;
    margin: 0 auto 10px;
}

.forecast-temp {
    font-size: 1.3rem;
    font-weight: 600;
    color: #00b894;
}

.forecast-time {
    font-size: 0.9rem;
    color: #636e72;
    margin-bottom: 5px;
}

.error-message {
    background: rgba(255, 99, 71, 0.9);
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin: 20px 0;
    display: none;
}

.error-message.hidden {
    display: none !important;
}

@media (max-width: 768px) {
    .current-temp {
        font-size: 3rem;
    }
    
    .weather-details {
        flex-direction: column;
        gap: 15px;
    }
    
    .forecast-grid {
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    }
}