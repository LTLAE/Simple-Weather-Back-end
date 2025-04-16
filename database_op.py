import mysql.connector
import os
from datetime import datetime

# for test

test_env = False
if test_env:
    db_host = "127.0.0.1"
    db_user = "backend"
    db_password = "Back3nd@LTLAE"
    db_name = "weather"
else:
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    print("Database environment:\nHost: ", db_host, "\nUser: ", db_user, "\nPassword: ", db_password, "\nDatabase: ", db_name)
    if db_host is None:
        print("Can't find DB_HOST, exiting...")
        exit(1)
    if db_user is None:
        print("Can't find DB_USER, exiting...")
        exit(1)
    if db_password is None:
        print("Can't find DB_PASSWORD, exiting...")
        exit(1)
    if db_name is None:
        print("Can't find DB_NAME, exiting...")
        exit(1)

# current weather table:
# city_name char(50) not null,
# region char(50),
# weather_main char(50),
# weather_description char(50),
# temp float,
# temp_feels_like float,
# pressure int,
# humidity int,
# visibility int,
# wind_speed float,
# wind_deg float,
# sunrise bigint,
# sunset bigint,
# last_updated datetime

def db_add_current_weather(city_name, lat, lon, region, weather_main, weather_description, temp, temp_feels_like, pressure, humidity, visibility, wind_speed, wind_deg, sunrise, sunset):
    # connect to db
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = db.cursor()
    # insert current weather info
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lat = round(lat, 4)
    lon = round(lon, 4)
    try:
        cursor.execute(f"delete from current_weather where city_name = '{city_name}'")
        cursor.execute(f"insert into current_weather values ('{city_name}', {lat}, {lon}, '{region}', '{weather_main}', '{weather_description}', {temp}, {temp_feels_like}, {pressure}, {humidity}, {visibility}, {wind_speed}, {wind_deg}, {sunrise}, {sunset}, '{last_updated}'); commit;")
        print("Inserted.")
    except Exception as e:
        print(f"Error: {e}")
    # close connection
    cursor.close()
    db.close()

def db_get_current_weather(lat, lon):
    # connect to db
    db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = db.cursor()
    # match latitude and longitude
    # current weather
    cursor.execute(f"select * from current_weather where abs(lat - {lat}) < 0.0001 and abs(lon - {lon}) < 0.0001")
    current = cursor.fetchall()
    # close connection
    cursor.close()
    db.close()
    return current

# 5d forecast table:
# city_name char(50) not null,
# lat float,
# lon float,
# region char(50),
# weather_main char(50),
# weather_description char(50),
# temp float,
# temp_feels_like float,
# pressure int,
# humidity int,
# visibility int,
# wind_speed float,
# wind_deg float,
# forecast_time datetime,
# last_updated datetime

def db_add_5d_weather(data_5d):
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = db.cursor()
    # insert current weather info
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lat = round(data_5d['city']['coord']['lat'], 4)
    lon = round(data_5d['city']['coord']['lon'], 4)
    try:
        cursor.execute(f"delete from 5d_forecast where city_name = '{data_5d['city']['name']}'")
        for timer in range(len(data_5d['list'])):
            cursor.execute(f"insert into 5d_forecast values ('{data_5d['city']['name']}', {lat}, {lon}, '{data_5d['city']['country']}', '{data_5d['list'][timer]['weather'][0]['main']}', '{data_5d['list'][timer]['weather'][0]['description']}', {data_5d['list'][timer]['main']['temp']}, {data_5d['list'][timer]['main']['feels_like']}, {data_5d['list'][timer]['main']['pressure']}, {data_5d['list'][timer]['main']['humidity']}, {data_5d['list'][timer].get('visibility', 0)}, {data_5d['list'][timer]['wind']['speed']}, {data_5d['list'][timer]['wind']['deg']}, '{data_5d['list'][timer]['dt_txt']}', '{last_updated}');")

        cursor.execute("commit;")
        print(len(data_5d['list']), " forecasts inserted.")
    except Exception as e:
        print(f"Error: {e}")
        # close connection
        cursor.close()
        db.close()

def db_get_5d_weather(lat, lon):
    # connect to db
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = db.cursor()
    # match latitude and longitude
    # current weather
    cursor.execute(f"select * from 5d_forecast where abs(lat - {lat}) < 0.0001 and abs(lon - {lon}) < 0.0001")
    weather_5d = cursor.fetchall()
    # close connection
    cursor.close()
    db.close()
    return weather_5d
