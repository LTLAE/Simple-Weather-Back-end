import requests
from database_op import *

# read api from file
with open('OpenWeatherMapAPI.txt', 'r') as f:
    api = f.read()


def search_city(city_name):
    # get latitude and longitude (geocoding)
    location_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={api}'
    location_response = requests.get(location_url)
    location_data = location_response.json()
    if location_response.status_code == 200:
        for timer in range(len(location_data)):
            # for demo only
            print(timer + 1, f" {location_data[timer]['name']}, {location_data[timer].get('state', ' ')}, {location_data[timer]['country']}")
            # this may change after we defined data structure

        user_selection = int(input("Select a location: ")) - 1
        return location_data[user_selection]['lat'], location_data[user_selection]['lon']

    else:
        print(f"Error: {location_data['message']}")
        return

def get_current_weather(lat, lon):
    # check if the city is already cached in db or expired (10 minutes)
    lat = round(lat, 4)
    lon = round(lon, 4)
    db_result = db_get_current_weather(lat, lon)
    if db_result:   # found in db
        # check if the data is expired
        last_updated = db_result[0][15]  # 15: last_updated
        time_elapsed = datetime.now() - last_updated
        if time_elapsed.total_seconds() < 600:  # not expired
            print("Get data from database successfully.")
            return db_result

    # not cached or expired, fetch data from api
    url_current = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
    response_current = requests.get(url_current)
    data_current = response_current.json()
    if response_current.status_code == 200:
        print("Get data from api successfully. Adding to database.")
        # add data to db
        db_add_current_weather(
            data_current['name'],
            data_current['coord']['lat'],
            data_current['coord']['lon'],
            data_current['sys']['country'],
            data_current['weather'][0]['main'],
            data_current['weather'][0]['description'],
            data_current['main']['temp'],
            data_current['main']['feels_like'],
            data_current['main']['pressure'],
            data_current['main']['humidity'],
            data_current['visibility'],
            data_current['wind']['speed'],
            data_current['wind']['deg'],
            data_current['sys']['sunrise'],
            data_current['sys']['sunset']
        )
    else:
        print(f"Error: {data_current['message']}")

    return data_current

def get_5d_weather(lat, lon):
    lat = round(lat, 4)
    lon = round(lon, 4)
    current_time = datetime.now()
    db_result = db_get_5d_weather(lat, lon)
    if db_result:   # found in db
        # check if the data is expired
        last_updated = db_result[0][15]  # 15: last_updated
        time_elapsed = datetime.now() - last_updated
        if time_elapsed.total_seconds() < 43200: # 12 hours
            print("Get data from database successfully.")
            # only return data after current time
            return [weather for weather in db_result if weather[14] > current_time]  # 14: forecast_time

