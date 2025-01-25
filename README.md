# Weather-Forecast-App
Weather App

Overview:
The Weather App is a Python-based application that allows users to fetch real-time weather data either for a specified city or for their current location. The app uses the OpenWeatherMap API (https://openweathermap.org/api) to retrieve weather information and displays it in a user-friendly format.

Features:
- Fetch weather data by city name.
- Automatically detect the user's current location using IP-based geolocation.
- Displays:
  - Temperature
  - Feels Like temperature
  - Weather description
  - Humidity
  - Wind Speed

Requirements:
- Python 3.x
- requests library

Setup Instructions:
1. Clone the Repository:
   git clone https://github.com/yashraz08/Weather-Forecast-App.git

2. Install Dependencies:
   Make sure you have Python 3.x installed. Then, install the required libraries using:
   pip install requests

3. API Key:
   To use the OpenWeatherMap API, you will need to replace the API_KEY in the script with your own. You can get an API key by signing up on the OpenWeatherMap website (https://openweathermap.org/api).

Usage:
1. Run the App:
   Navigate to the project folder and run the script:
   python weather_forecast_app.py

2. How it Works:
   - The app will first try to fetch the weather for your current location based on your IP address.
   - After displaying the weather for your location, you will be prompted to enter the name of a city to get the weather information for that city.

3. Example Output:
   Weather App
   Weather for your current location (New York):
   City: New York
   Temperature: 15°C
   Feels Like: 12°C
   Weather: Clear sky
   Humidity: 70%
   Wind Speed: 3.5 m/s
   Enter city name: London
   City: London
   Temperature: 10°C
   Feels Like: 8°C
   Weather: Overcast clouds
   Humidity: 80%
   Wind Speed: 4.0 m/s

Notes:
- Make sure you have a stable internet connection to fetch weather data.
- If you reach the API limit for requests, you may need to wait or upgrade to a premium plan on OpenWeatherMap.
- The app uses IP-based geolocation to determine your location, so it may not always be 100% accurate.

License:
This project is licensed under the MIT License - see the LICENSE file for details.
