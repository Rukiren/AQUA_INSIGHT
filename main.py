from import_file.watter import get_name, caculator_River_info ,get_River_info
from import_file.loaction_google import transfer_place_to_coord
from import_file.weather import weather
from import_file.wild_animal import get_animal
import json
from import_file.command import gpt35

#生成json檔
def generate_data_address(address):
    coord = transfer_place_to_coord(address)
    coord_x = coord[0]
    coord_y = coord[1]
    
    
    # ======= River ========= #
    print("正在抓取水域資料...")
    
    River_name = get_name(coord_x, coord_y)
    pH, WT, PRI, PRI_NAME = caculator_River_info(River_name)
    River_name = River_name +"("+ gpt35("你是名翻譯員，請將輸入的河流名稱轉換為正確的英文河流名稱，使用英文", River_name)+")"
    
    # water parameter trasfer to json format
    water = { 'river_name' : River_name, 'pH' : pH, 'water_temperature' : WT, 'pollution_level' : PRI, 'pollution_level_name' : PRI_NAME }
    
    with open("static/water.json", 'w') as f:
        json.dump(water, f)
        
    # ======= weather ========= #
    print("正在抓取天氣資料...")
        
    weather_info = weather(coord_x, coord_y)

    # weather parameter trasfer to json format
    weather_json = {'current_time' : str(weather_info[0]), 'probability_of_precipitation' : str(weather_info[1]),'weather_info' : str(weather_info[2])}
    
    with open("static/weather.json", 'w') as f:
        json.dump(weather_json, f)
    
    
    # ======= animal ========= #
    print("正在抓取生物資料...")
    
    
    animal = get_animal(coord_x, coord_y)
    #animal = json.loads(animal_str)
    
    with open("static/animal.json", 'w') as f:
        f.write(animal)
    
        
    # ======= print ========= #
    print("執行完成")
    print("======================")
    
def generate_data_coordinate(coord_x, coord_y):
    
    # ======= River ========= #
    print("正在抓取水域資料...")
    
    River_name = get_name(coord_x, coord_y)
    pH, WT, PRI, PRI_NAME = caculator_River_info(River_name)
    
    # water parameter trasfer to json format
    water = { 'river_name' : River_name, 'pH' : pH, 'water_temperature' : WT, 'pollution_level' : PRI, 'pollution_level_name' : PRI_NAME }
    
    with open("static/water.json", 'w') as f:
        json.dump(water, f)
        
    # ======= weather ========= #
    print("正在抓取天氣資料...")
        
    weather_info = weather(coord_x, coord_y)

    # weather parameter trasfer to json format
    weather_json = {'current_time' : str(weather_info[0]), 'probability_of_precipitation' : str(weather_info[1]),'weather_info' : str(weather_info[2])}
    
    with open("static/weather.json", 'w') as f:
        json.dump(weather_json, f)
    
    
    # ======= animal ========= #
    print("正在抓取生物資料...")
    
    
    animal = get_animal(coord_x, coord_y)
    #animal = json.loads(animal_str)
    
    with open("static/animal.json", 'w') as f:
        f.write(animal)
    
        
    # ======= print ========= #
    print("執行完成")
    print("======================")

