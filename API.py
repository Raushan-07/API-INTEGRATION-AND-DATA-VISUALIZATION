import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your OpenWeatherMap API Key
API_KEY = '5d7af2ef0c9eec6778a703ae9ee60e33'

# List of cities to fetch weather for
cities = ['Ranchi', 'Daltonganj', 'Jamshedpur', 'Delhi', 'Dhanbad', 'karnataka', 'Ramgarh', 'patna']

# Base URL
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Lists to store data
city_names = []
temperatures_celsius = []

# Fetch weather data
for city in cities:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        city_names.append(city)
        temperatures_celsius.append(temp)
        print(f"{city}: {temp}°C")
    else:
        print(f"Failed to get data for {city}: {data.get('message')}")

# Visualization using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(9, 6))
sns.barplot(x=city_names, y=temperatures_celsius,hue=city_names, palette='deep')
plt.title('Current Temperatures in Major Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.tight_layout()

# Save and show the dashboard
plt.savefig('weather_dashboard.png')
plt.show()