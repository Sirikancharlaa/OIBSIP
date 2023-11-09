import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.location_entry = ttk.Entry(self.master)
        self.location_entry.grid(row=0, column=0, padx=10, pady=10)

        self.search_button = ttk.Button(self.master, text="Search", command=self.get_weather)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def get_weather(self):
        api_key = 'YOUR_API_KEY'
        location = self.location_entry.get()
        if not location:
            self.result_label.config(text="Please enter a location.")
            return

        try:
            # Get weather data from OpenWeatherMap API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            # Parse and display weather information
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            result_text = f"Weather in {location}:\n"
            result_text += f"Condition: {weather_description}\n"
            result_text += f"Temperature: {temperature}°C\n"
            result_text += f"Humidity: {humidity}%\n"
            result_text += f"Wind Speed: {wind_speed} m/s"

            self.result_label.config(text=result_text)

        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
