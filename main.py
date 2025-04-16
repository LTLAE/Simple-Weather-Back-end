from functions import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search_city', methods=['POST'])
def search_city():
    receive = request.get_json()
    city = receive['city']
    return jsonify(get_city_list(city))

@app.route('/get_current_weather', methods=['POST'])
def send_current_weather():
    receive = request.get_json()
    lat = receive['lat']
    lon = receive['lon']
    current_weather = get_current_weather(lat, lon)
    current_weather += [AI_recommendation(current_weather)]
    return jsonify(current_weather)

@app.route('/get_5d_weather', methods=['POST'])
def send_5d_weather():
    receive = request.get_json()
    lat = receive['lat']
    lon = receive['lon']
    weather_5d = get_5d_weather(lat, lon)
    return jsonify(weather_5d)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

