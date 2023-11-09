import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    # Replace 'YOUR_API_KEY' with a valid OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(base_url)
        weather_data = response.json()

        # Extract relevant weather information
        main_info = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        return f'{main_info}: {description}\nTemperature: {temperature}°C'
    except Exception as e:
        return f'Error fetching weather data: {e}'

def get_location():
    # For simplicity, you can use a placeholder for location.
    # In a real application, you would use a library like geopy for more accuracy.
    return "City, Country"

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning('Warning', 'Please enter a city.')
        return

    weather_info = get_weather(city)
    result_label.config(text=weather_info)

def fetch_location_weather():
    location = get_location()
    weather_info = get_weather(location)
    result_label.config(text=weather_info)

# GUI setup
app = tk.Tk()
app.title('Weather App')

# Input widgets
city_label = tk.Label(app, text='Enter City:')
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

# Buttons
get_weather_button = tk.Button(app, text='Get Weather', command=fetch_weather)
get_weather_button.pack(pady=10)

get_location_button = tk.Button(app, text='Get Location Weather', command=fetch_location_weather)
get_location_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text='')
result_label.pack(pady=10)

# Run the app
app.mainloop()
