from import_file.watter import get_name, caculator_River_info ,get_River_info
from import_file.loaction_google import transfer_place_to_coord
from import_file.weather import weather
from import_file.wild_animal import get_animal
import json

def generate_data(address):
    coord = transfer_place_to_coord(address)
    coord_x = coord[0]
    coord_y = coord[1]
    
    
    # ======= River ========= #
    
    River_name = get_name(coord_x, coord_y)
    pH, WT, PRI, PRI_NAME = caculator_River_info(River_name)
    
    # water parameter trasfer to json format
    water = { 'river_name' : River_name, 'pH' : pH, 'water_temperature' : WT, 'pollution_level' : PRI, 'pollution_level_name' : PRI_NAME }
    
    with open("static/water.json", 'w') as f:
        json.dump(water, f)
        
    # ======= weather ========= #
        
    weather_info = weather(coord_x, coord_y)

    # weather parameter trasfer to json format
    weather_json = {'current_time' : str(weather_info[0]), 'probability_of_precipitation ' : str(weather_info[1]),'weather_info' : str(weather_info[2])}
    print(weather_json)
    
    
    with open("static/weather.json", 'w') as f:
        json.dump(weather_json, f)
    
    
    # ======= animal ========= #
    
    animal_str = get_animal(coord_x, coord_y)
    animal = json.loads(animal_str)
    
    with open("static/animal.json", 'w') as f:
        json.dump(animal, f)
    
        
    # ======= print ========= #
    
    '''
    print(f"離您最近的河流為:{River_name}\n該河流月均 pH 值為：{pH}\n該河流月均水溫為:{WT}\n該河流污染狀況為:{PRI_NAME}")
    print(weather_info[2])
    print(animal)
    '''

