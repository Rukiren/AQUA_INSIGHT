import requests
import json
from geopy.distance import geodesic

def get_River_info():
    """ 
    取得所有河流資訊
    get_River_info()
    """
    # API的URL
    api_url = 'https://data.moenv.gov.tw/api/v2/wqx_p_01'

    params = {
        'language': 'zh',
        'limit': '10000',
        'api_key': 'f434a7dd-2918-43ef-8bd6-3918b6c4c9cb'
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
    
        with open('River_data.json', 'wb') as file:
            file.write(response.content)
        print("河流資訊成功下載並保存到 River_data.json 文件中")
    else:
        print("河流資訊下載失敗:", response.status_code)

def get_name(x, y):
    """ 
    取得經緯度最近河流
    get_name(x,y)
    x: 經度
    y: 緯度
    """
    with open('River_data.json', 'r') as file:
        data = json.load(file)

    min_distance = float('inf')
    name = None

    my_location = (float(x), float(y))

    for i in data["records"]:
        site_loaction = (float(i["twd97lat"]), float(i["twd97lon"]))

        distance = geodesic(my_location, site_loaction).kilometers

        if distance < min_distance:
            min_distance = distance
            name = i["river"]

    return name

def caculator_River_info(name):
    """ 
    根據河流名稱取得河流資訊
    caculator_River_info(name)
    name: 河流名稱

    Output:
    pH: 酸鹼值
    Water_temerature: 水溫
    PRI: PRI 值
    PRI_NAME: PRI 污染程度分類
    """
    with open('River_data.json', 'r') as file:
        data = json.load(file)

    pH = None
    Water_temperature = None
    PRI = None
    PRI_NAME = None
    Temperature = None
    
    for i in data["records"]:
        if i["river"] == name:
            if i["itemname"] == "酸鹼值":
                pH = float(i["itemvalue"])
            elif i["itemname"] == "水溫":
                Water_temperature = float(i["itemvalue"])
            elif i["itemname"] == "河川污染分類指標":
                PRI = float(i["itemvalue"])
                if PRI < 1:
                    PRI_NAME = "未（稍）受污染"
                elif PRI < 3:
                    PRI_NAME = "輕度污染"
                elif PRI < 6:
                    PRI_NAME = "中度污染"
                else:
                    PRI_NAME = "嚴重污染"
    return(pH, Water_temperature, PRI, PRI_NAME)

def get_River_photo(x, y):
    KEY = "dS5EGVg8Gz0PhFm35iDLM7La5FnGTk4fJtF7ooGc"
    with open('River_data.json', 'r') as file:
        data = json.load(file)

    min_distance = float('inf')
    xx = None
    yy = None

    my_location = (float(x), float(y))

    for i in data["records"]:
        site_loaction = (float(i["twd97lat"]), float(i["twd97lon"]))

        distance = geodesic(my_location, site_loaction).kilometers

        if distance < min_distance:
            min_distance = distance
            xx = i["twd97lat"]
            yy = i["twd97lon"]
    url = f"https://api.nasa.gov/planetary/earth/imagery?lon={xx}&lat={yy}&date=2014-02-01&api_key={KEY}"
    response = requests.get(url)
    return response.url
