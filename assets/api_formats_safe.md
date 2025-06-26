API formats for Simple Weather  
----

By Longtail Amethyst Eralbrunia  

## API Introductions  
In backend flask server, there are 3 available APIs  
- /search_city  
- /get_current_weather  
- /get_5d_weather

The general workflow will be like:  
Frontend: search_city(city_name)  
Backend: List of available cities [(City_name, lat, lon),(),...]  
Frontend: get_current_weather(lat, lon)
Backend: Weather data&AI recommendations [[City_name, lat, lon, Region, Weather_main, Weather_description, temperature, temperature_feels_like, pressure, humidity, visibility, wind_speed, wind_degree, sunrise_time, sunset_time], AI_recommendations]  
Frontend: get_5d_weather(lat, lon)  
Backend: Weather data in list [[City_name, lat, lon, Region, Weather_main, Weather_description, temperature, temperature_feels_like, pressure, humidity, visibility, wind_speed, wind_degree, time],[],...]  

## Data structure  
All backend response would be sent via json format.  
Most of response data structure are showed above.  

## How to send response
Send parameters in body.
- Search city: 
```json
city: "city_name"
```
- Get current weather: 
```json
lat: latitude,
lon: longitude
```
- Get 5d weather: 
```json
lat: latitude,
lon: longitude
```

For example:  
```json
fetch('http://127.0.0.1:5000/get_current_weather', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        lat: 22.1899,
        lon: 113.538
    })
})
```
In this example, frontend would send latitude and longitude to backend, and backend would return the current weather data and AI recommendations.

Since I don't know much about html and json, I would try to explain how it work with a example by chatGPT.
```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>获取当前天气</title>
</head>
<body>
    <h1>当前天气信息</h1>
    <button id="getWeatherButton">获取天气</button>
    <pre id="weatherResult"></pre>

    <script>
        document.getElementById("getWeatherButton").addEventListener("click", function() {
            fetch('http://127.0.0.1:5000/get_current_weather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    lat: 22.1899,
                    lon: 113.538
                })
            })
            .then(response => response.json())
            .then(data => {
                let resultDiv = document.getElementById("weatherResult");
                resultDiv.textContent = JSON.stringify(data, null, 2);  // 直接显示原始数据
            })
            .catch(error => {
                console.error("获取天气信息失败:", error);
                let resultDiv = document.getElementById("weatherResult");
                resultDiv.textContent = "无法获取天气信息，请稍后再试。";
            });
        });
    </script>
</body>
</html>
```

## If you want to test your code...
I have set up a cloud server with backend only for test. You can change the fetch address to  
```
http://****************/<api>
```
For example:  
```
http://****************/get_current_weather
```
**Please be aware that this server is only for test only.**  
**Please do not leak this address to public, because any leak of IP address of this server would cause potential attacks.**  
**Please do not keep server address in the code, it means that you are leaking the address. Instead, read the address from a config file.**