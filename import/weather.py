import requests
import json
import datetime

def UT_To_datetime(ut):
    dt = datetime.datetime.fromtimestamp(ut)
    return dt

def weather (lat,lon):
    api_key="58933e3243e67ee261b7f03b110f5dab"
    url="https://api.openweathermap.org/data/3.0/onecall?lat=%s&lon=%s&appid=%s&lang=zh_tw&units=metric" % (lat, lon, api_key)
    print(url)
    weather_request=requests.get(url)
    data = json.loads(weather_request.text)
    current_time = UT_To_datetime(int(data["current"]["dt"]))
    print(current_time)
    print("------------------------------------------------------------------------------------------------")
    current=data["current"]
    print(current)
    print("------------------------------------------------------------------------------------------------")
    hourly=data["hourly"]
    print(hourly)
    print("------------------------------------------------------------------------------------------------")
    print(hourly[0])
    print("------------------------------------------------------------------------------------------------")
    daily=data["daily"]
    print(daily)
    print("------------------------------------------------------------------------------------------------")
    print(daily[0])
weather(24.1450321,120.6716122)


