import requests
import json
import datetime
from . import command


def UT_To_datetime(ut):
    dt = datetime.datetime.fromtimestamp(ut)
    return dt

def weather (lat,lon):
    """ 
    輸入緯度,經度
    weather(lat, lon)
    lat: 經度
    lon: 緯度

    return 現在時間,降雨機率,氣象預報
    """
    api_key="58933e3243e67ee261b7f03b110f5dab"
    url="https://api.openweathermap.org/data/3.0/onecall?lat=%s&lon=%s&appid=%s&lang=zh_tw&units=metric" % (lat, lon, api_key)
    #print(url)
    weather_request=requests.get(url)
    data = json.loads(weather_request.text)
    current_time = UT_To_datetime(int(data["current"]["dt"]))
    #print(current_time)
    #print("------------------------------------------------------------------------------------------------")
    current=data["current"]
    hourly=data["hourly"]
    pop=hourly[0]["pop"]
    #print(pop)
    #print("------------------------------------------------------------------------------------------------")
    opt = command.gpt35("你是一名氣象預報專家，請依據輸入的各項數值，給出當日簡短的天氣建議，使用英文", str(current))
    #
    # print(opt)
    #print(type())
    all = [current_time,pop,opt]
    #print(all)
    return all
#weather(24.1450321,120.6716122)
    

