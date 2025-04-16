-- init.sql
drop user if exists 'backend'@'%';
create user 'backend'@'%' identified by 'Back3nd@LTLAE';

create database if not exists weather;

grant select, insert, update, delete on weather.* to 'backend'@'%';

flush privileges;

use weather;
drop table if exists current_weather;
create table current_weather (
    city_name char(50) primary key not null,
    lat float,
    lon float,
    region char(50),
    weather_main char(50),
    weather_description char(50),
    temp float,
    temp_feels_like float,
    pressure int,
    humidity int,
    visibility int,
    wind_speed float,
    wind_deg float,
    sunrise bigint,
    sunset bigint,
    last_updated datetime
);

drop table if exists 5d_forecast;
create table 5d_forecast (
    city_name char(50) not null,
    lat float,
    lon float,
    region char(50),
    weather_main char(50),
    weather_description char(50),
    temp float,
    temp_feels_like float,
    pressure int,
    humidity int,
    visibility int,
    wind_speed float,
    wind_deg float,
    forecast_time datetime,
    last_updated datetime
);

commit;