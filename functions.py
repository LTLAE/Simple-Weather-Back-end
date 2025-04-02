import requests

from ai_recommendation import fetch_from_AI
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
        search_results = []
        for timer in range(len(location_data)):
            search_results.append({
                'name': location_data[timer]['name'],
                'state': location_data[timer].get('state', ' '),
                'country': location_data[timer]['country'],
                'lat': location_data[timer]['lat'],
                'lon': location_data[timer]['lon']
            })

        return search_results

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
        last_updated = db_result[0][14]  # 14: last_updated
        time_elapsed = datetime.now() - last_updated
        if time_elapsed.total_seconds() < 43200:  # 12 hours
            print("Get data from database successfully.")
            # get rid of past data
            while True:
                forecast_time = db_result[0][13]  # 13: forecast_time
                if forecast_time > current_time:
                    break
                db_result.remove(db_result[0])

            return db_result

    # not cached or expired, fetch data from api
    url_5d = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}'
    response_5d = requests.get(url_5d)
    data_5d = response_5d.json()
    if response_5d.status_code == 200:
        print("Get data from api successfully. Adding to database.")
        # get rid of past data
        while True:
            forecast_time = datetime.strptime(data_5d['list'][0]['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if forecast_time > current_time:
                break
            data_5d['list'].remove(data_5d['list'][0])
        # add to db
        db_add_5d_weather(data_5d)

    else:
        print(f"Error: {data_5d['message']}")

    return data_5d

def AI_recommendation(weather_data_raw):
    recommend_prompt = "你是一位专业的天气数据分析师，你正在向大众展示分析天气。稍后我会给你提供一些天气信息，总结这些天气数据的特点，给出大众准确且恰当的穿衣建议和出行建议。你总共需要回复两句话，第一句话包含穿衣建议，如衣服类型、颜色等；第二句话包含出行建议，如适合的户外活动、出行方式等。"
    weather_data_raw = str(weather_data_raw)
    return fetch_from_AI("DS", recommend_prompt, weather_data_raw)
