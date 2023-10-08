import googlemaps

# ntcu latitude = (24.142877780232975, 120.6720582676029) # ntcu latitude

def get_location(): # 取得現在位置經緯度
    API_key = "AIzaSyBlkm0dQ8VE9HdSXuV_68UBcAoXy8SLn_g"
    gmaps = googlemaps.Client(key=API_key)
    location = gmaps.geolocate()
    return [location['location']['lat'], location['location']['lng']]

def transfer_place_to_coord(addr):
    """ 
    地址轉換成經緯度
    transfer_place_to_coord(addr)
    addr: 地址

    Output: [x,y]
    """ # 地址轉換成經緯度
    API_key = "AIzaSyBlkm0dQ8VE9HdSXuV_68UBcAoXy8SLn_g"
    gmaps = googlemaps.Client(key=API_key)
    coord = gmaps.geocode(address = addr)
    # print(coord)
    
    return [coord[0]['geometry']['location']['lat'],coord[0]['geometry']['location']['lng']]

if __name__ == '__main__':
    location = get_location()
    address = "台中市西區"
    test = transfer_place_to_coord(address)
    print(test)






