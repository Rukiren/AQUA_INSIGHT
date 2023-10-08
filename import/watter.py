import requests

def get_River_info():
    # API的URL
    api_url = 'https://data.moenv.gov.tw/api/v2/wqx_p_01'

    params = {
        'language': 'zh',
        'limit': '10000',
        'api_key': 'f434a7dd-2918-43ef-8bd6-3918b6c4c9cb'
    }

    ## get 河流 json
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        # 存檔
        with open('River_data.json', 'wb') as file:
            file.write(response.content)
        print("河流資訊下載成功")
    else:
        print("河流資訊下載失敗，狀態:", response.status_code)
