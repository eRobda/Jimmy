import requests

def get_weather(lat, len):
    response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=a6d9f7d543ea4ecb81675134242104&q={lat}, {len}&days=3&aqi=no&alerts=no")
    print(response.json())

get_weather(50.43929175445562, 15.766406194127955)