import requests as req
from requests import *
from bs4 import BeautifulSoup
import wikipediaapi
from . import command

#將維基百科資訊段落存進list
def load_sections(sections, title_list, content_list, level=0):
        for s in sections:
            title_list.append(s.title)
            content_list.append(s.text)
            load_sections(s.sections, title_list, content_list, level + 1)

#經緯度座標
def coordinate(coord_x,coord_y):
    url = "https://www.tbn.org.tw/api/v25/occurrence?circle={} {},13&limit=20".format(coord_x,coord_y) #x座標,y座標,半徑(km),資料量
    response = req.get(url)
    
    uuid_list = []
    
    if response.status_code ==200:
        print("UUID - 生物UUID資料抓取成功")
        
        data = response.json() #抓下來的資料轉json格式
        uuid_counter = 0
        
        for i in data['data']:
            if uuid_counter ==10:
                break
            for uuid in i:
                if uuid == "taxonUUID":
                    
                    #測試是否重複
                    exist = False
                    for element in uuid_list:
                        if(element == i[uuid]):
                            exist = True
                            break
                        
                    if i[uuid] == None:
                        continue
                    else:
                        if(exist):
                            continue
                        else:
                            uuid_list.append(i[uuid]) #將生物UUID存成一個list
                            uuid_counter+=1
    else:
        print("UUID - 生物UUID資料資料抓取失敗")
        
    #print(uuid_list)
    return uuid_list
    

#透過UUID搜尋生物
def search(uuid):
    
    name_list = [] #物種名稱
    group_list = [] #種族
    IUCN_list= [] #危險等級(ICNU)
    pic_list = [] #物種照片超連結
    
    title_list = [] #物種介紹標題
    content_list = [] #物種介紹內容
    intro_list = [] #物種介紹
    
    for i in uuid:
        url = "https://www.tbn.org.tw/api/v25/taxon?uuid={}".format(i) #抓取將陣列的每一個UUID的生物資訊
        response = req.get(url) 
        
        
        if response.status_code ==200:
            #print("資料抓取成功")
            
            datas = response.json() #抓下來的資料轉json格式
            
            for data in datas['data']:
                for result in data: 
                    
                    # 物種名稱
                    if result == "simplifiedScientificName":
                        name_list.append(data[result]) #將物種學名存成一個list
                    
                    # 物種種族
                    if result == "taxonGroup":
                        group_list.append(data[result]) #將生物種族存成一個list
                    
                    # 瀕危指數
                    if result == "categoryIUCN":
                        IUCN_list.append(data[result]) #將瀕危指數等級存成一個list
                    
        else:
            print("資料抓取失敗")
    
    
    #從學名抓取相關物種圖片
    for i in name_list:
        
        url = "https://www.inaturalist.org/search?q={}".format(i) #去iNaturalist網站搜尋
        response = req.get(url) 
        soup = BeautifulSoup(response.text, 'html.parser') 
        
        if response.status_code ==200:
            #print("網頁訪問成功")
            pic_element = soup.find(class_="inner").find("a").find("img")
            
            if(pic_element):
                pic_url = pic_element.get('src')
                pic_url = pic_url.replace("square","medium")
                pic_list.append(pic_url)
            else:
                print("圖片 - 未抓取到物種 {} 圖片".format(i))
                pic_list.append(None)
        else:
            print("網頁訪問失敗")
            
    
    ''''''
    #從學名抓取wikipedia物種介紹
    for i in name_list: 
        wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'zh')
        page_py = wiki_wiki.page(i)
        
        if(page_py):
            #print("wiki資料抓取成功")
            load_sections(page_py.sections, title_list, content_list) #將維基百科資訊段落存進list
        else:
            print("Wiki - {} 資料抓取失敗".format(i))
            title_list.append(None)
            content_list.append(None)
       
    intro_list = [title_list,content_list] #將段落存成一個list
    ''''''''''''''''''
    
    ''' 
            
    print("-------------------")
    print(name_list)
    print("-------------------")
    print(group_list)
    print("-------------------")
    print(IUCN_list)
    print("-------------------")
    print(pic_list)
    print("-------------------")
    print(intro_list)
    print("-------------------")
    
    '''
    
    all = [name_list, group_list, IUCN_list, pic_list] # [物種學名, 物種類別, 物種瀕危指數, 物種圖片連結]
    animal_info = command.gpt35("你是一個生態保育專家，請進行簡單有趣的科普，科普資訊存為<<info>>，生物學名請使用中文，輸出格式為一個 json，animal: anima_1{name, photo_link, <<info>>}", str(all))
    
    
    return animal_info    

def get_animal(lat,lon): #緯度,經度
    str = search(coordinate(lon,lat))
    return str
    
    
    
# ======= main =========


#get_animal(24.1532928,120.6779904) #緯度,經度
#get_picture(coordinate(120.6779904,24.1532928))



