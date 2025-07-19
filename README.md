# API-INTEGRATION-AND-DATA-VISUALIZATION

**COMPANY*: CODTECH

*NAME*: RAUSHAN KUMAR

*INTERN ID*: CT06DG962

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*/MENTOR*: NEELA SANTOSH KUMAR**


📌 **Project Overview**

This project demonstrates the integration of a public API—specifically, the OpenWeatherMap API—with data visualization tools in Python. The objective is to fetch real-time weather data (temperature) for various Indian cities and visualize the data using Seaborn and Matplotlib, two of the most powerful Python libraries for data plotting.
The resulting dashboard provides a bar chart comparing current temperatures across a list of selected cities. This exercise enhances understanding of REST API usage, JSON parsing, Python requests handling, and data visualization techniques.

🧰**Technologies Used**



Requests – for API calls

Seaborn – for data visualization

Matplotlib – for creating and saving plots

OpenWeatherMap API – to fetch real-time weather data

 **Project Features**
 


Connects to the OpenWeatherMap API using HTTP GET requests.

Parses JSON responses to extract temperature data.

Stores temperature and city data in lists.

Handles API errors and displays failure messages.

Visualizes temperatures for various cities using a bar chart.

Saves the visualization as a PNG image (weather_dashboard.png).


**Learning Objectives**



By working on this project, you’ll:

Learn how to access and consume data from a RESTful API.

Understand how to handle JSON responses in Python.

Gain experience in error handling for failed HTTP requests.

Explore Seaborn's capabilities for aesthetic plotting.

Get familiar with real-world data wrangling and visualization tasks.

 **Cities Included**

 

 
This script fetches temperature data for the following Indian cities:

Ranchi

Daltonganj

Jamshedpur

Delhi

Dhanbad

Karnataka

Ramgarh

Patna


**Getting Started**




1. Clone the Repository
git clone https://github.com/yourusername/weather-api-dashboard.git
cd weather-api-dashboard

2. Install Dependencies
Ensure Python is installed, then run:
pip install requests matplotlib seaborn

3. Run the Script
Replace API_KEY in the script with your personal OpenWeatherMap API key (you can get it for free at openweathermap.org).
python weather_dashboard.py

**Code Explanation**


API Integration
The script uses the requests library to make an HTTP GET call to the OpenWeatherMap API. The API endpoint is:
https://api.openweathermap.org/data/2.5/weather
Each city’s weather data is fetched using query parameters:

q: City name

appid: Your API key

units: Set to "metric" for Celsius

Data Parsing
The JSON response is parsed to extract the temperature using:
temp = data['main']['temp']

**Visualization**



The data is visualized using a barplot from Seaborn:
sns.barplot(x=city_names, y=temperatures_celsius, hue=city_names)
The chart is saved as:
plt.savefig('weather_dashboard.png')
📂 Project Structure
weather-api-dashboard/
│
├── weather_dashboard.py       # Main script file
├── weather_dashboard.png      # Generated visualization (after running the script)
├── README.md                  # This file

**Notes**



Ensure your internet connection is stable while running the script.

City names must be valid as per OpenWeatherMap API's recognition.

Do not expose your API key publicly in shared repositories.

**Sample Output**




<img width="976" height="724" alt="image" src="https://github.com/user-attachments/assets/590aa64b-d5dd-45c3-9f82-67a420319a7a" />

🤝 **Acknowledgments**
OpenWeatherMap
Seaborn Documentation
Matplotlib Documentation
