import requests
import tkinter as tk
from tkinter import Label, Button

def get_weather():
    city = entry.get()
    api_key = '2c8b95ba8a4de03d11ffc84db5049afc'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    print(f'HTTP response status_code = {response.status_code}')
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    temp_in_C = round(temperature - 273.15, 2)
    temp_in_F = round((temp_in_C * 9/5) + 32, 2)

    description = weather_data['weather'][0]['description']
    result_label.config(text=f"Current weather in {city}: {description}\nTemperature: {temp_in_C}°C or {temp_in_F}°F", fg="white")

# Create a simple Tkinter window
root = tk.Tk()
root.title("Weather App")

# Set the background color to black
root.configure(bg="blue")

# Create and place widgets in the window
label = Label(root, text="Enter city:", bg="black", fg="white")
label.pack(padx=10,pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

get_weather_button = Button(root, text="Get Weather", command=get_weather, bg="green", fg="orange")
get_weather_button.pack(pady=10)

result_label = Label(root, text="", bg="black", fg="white")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
