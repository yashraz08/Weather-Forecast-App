import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        messagebox.showerror("Error", f"Failed to connect to the weather service.\n{e}")
        return None
# Function to fetch current location using IP-based geolocation
def get_current_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()
        return data.get("city")
    except requests.exceptions.RequestException:
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
        return "Could not fetch weather data for your location."
# Function to display weather for user-entered city
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    result_label.config(text="Fetching weather data...")
    app.update_idletasks()

    result = display_weather(city)
    result_label.config(text=result)
# Function to automatically display weather for the current location
def display_current_location_weather():
    city = get_current_location()
    if city:
        result = display_weather(city)
        current_location_weather_label.config(text=result)
    else:
        current_location_weather_label.config(text="Could not detect your current location. Please check your internet connection.")
# Create the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x500")
app.resizable(False, False)
# Create and arrange widgets
tk.Label(app, text="Weather Forecast", font=("Helvetica", 18, "bold")).pack(pady=10)
# Label to show current location weather
current_location_weather_label = tk.Label(app, text="Loading current location weather...", font=("Helvetica", 12), justify="left")
current_location_weather_label.pack(pady=10)
# Label for city input
tk.Label(app, text="Enter City Name:", font=("Helvetica", 12)).pack(pady=5)
# Entry box for city name
city_entry = tk.Entry(app, font=("Helvetica", 12), width=30, justify="center")
city_entry.pack(pady=5)
# Button to fetch weather data for the city entered
get_weather_button = tk.Button(app, text="Get Weather for City", font=("Helvetica", 12), command=get_weather)
get_weather_button.pack(pady=10)

# Label to display weather result
result_label = tk.Label(app, text="", font=("Helvetica", 12), justify="left", width=40, height=6, relief="solid", anchor="nw", padx=10, pady=5)
result_label.pack(pady=10)

# Style for loading spinner
style = ttk.Style()
style.configure("TProgressbar", thickness=30)

# Automatically display current location weather
display_current_location_weather()

# Run the application
app.mainloop()
