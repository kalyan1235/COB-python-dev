import requests
import csv


api_key = '143123cac47fdcac6b9c2be8cdfa9619'
city = 'London'

# Fetching weather data from the API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extracting relevant data
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    # Writing data to CSV file
    with open('weather_data.csv', mode='w', newline='') as file:
        fieldnames = ['City', 'Temperature (Celsius)', 'Humidity', 'Description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'City': city_name, 'Temperature (Celsius)': temperature, 'Humidity': humidity, 'Description': weather_description})

    print(f"Weather data for {city_name} has been saved to 'weather_data.csv'")
else:
    print("Failed to fetch weather data. Please check your API key or city name.")