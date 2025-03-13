# Flask Weather App 🌦️

A simple Flask-based web application that fetches weather data based on user input.

## Features 🚀
- Fetch real-time weather data using an API.
- Display temperature, weather conditions, and "feels like" temperature.
- Handle invalid city names with a custom error page.

## API Used 🌍
This application fetches weather data from OpenWeather API (or any other weather API you are using).  



## Installation 🛠️

Run the following commands step by step in your terminal:

```sh
# Clone the repository
git clone https://github.com/qy1206/flask-weather-app.git
cd flask-weather-app

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python server.py


