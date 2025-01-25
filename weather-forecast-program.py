import requests
# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city):
    API_KEY = "ae01bc2e968a0d0251f9c371cf066f20" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the weather service.\n{e}")
        return None
# Function to fetch current location using IP-based geolocation
def get_current_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()
        return data.get("city")
    except requests.exceptions.RequestException:
        print("Error: Could not detect your current location.")
        return None
# Function to display weather data
def display_weather(city):
    data = get_weather_data(city)
    if data and "main" in data:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (
            f"City: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Weather: {weather_desc}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    else:
        return "Could not fetch weather data for the specified location."
# Function to get weather for a user-entered city
def get_weather_for_city():
    city = input("Enter city name: ").strip()
    if not city:
        print("Error: Please enter a valid city name.")
        return
    result = display_weather(city)
    print(result)
# Function to display weather for the current location
def display_current_location_weather():
    city = get_current_location()
    if city:
        result = display_weather(city)
        print(f"Weather for your current location ({city}):\n{result}")
    else:
        print("Could not detect your current location. Please check your internet connection.")
# Main execution
if __name__ == "__main__":
    print("Weather App")
    display_current_location_weather()
    get_weather_for_city()
