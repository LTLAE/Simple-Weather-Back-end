from functions import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# for test only
# input_city = input("Enter city name: ")
# lat, lon = search_city(input_city)
# current_weather = get_current_weather(lat, lon)
# print(f"City: {current_weather[0][0]}")
# print(f"Location: {current_weather[0][1]}, {current_weather[0][2]}")
# print(f"Weather: {current_weather[0][4]}")
# temperature = round(current_weather[0][6] - 273.15, 1)
# print(f"Temperature: {temperature} °C")

@app.route('/getcurrentweather', methods=['POST'])
def send_current_weather():
    receive = request.get_json()
    city = receive['city']
    lat, lon = search_city(city)
    current_weather = get_current_weather(lat, lon)
    return jsonify(current_weather)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

