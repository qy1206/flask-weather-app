from flask import Flask, render_template, request
from weather import get_current_weather


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

  
    if not bool(city.strip()):
     
        city = "Kansas City"

    weather_data = get_current_weather(city)
    print("API Response:", weather_data)  

    if str(weather_data.get('cod')) != "200":
        print("City not found, rendering city-not-found.html")
        return render_template('city-not-found.html')


    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, use_reloader=False, use_debugger=True, host="0.0.0.0", port=8000)

