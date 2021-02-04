import requests
import os
import pprint

key = os.environ['key']
token = os.environ['token']

def Updates():
    url_update = f'https://api.telegram.org/bot{token}/getUpdates'
    respons = requests.get(url=url_update)
    data = respons.json()['result']
    last_msg = data[-1]

    return last_msg

# payload = {
#     'appid': key,
#     'q': 'Bulung\'ur'
# }
# url = f'https://api.openweathermap.org/data/2.5/weather'
# respons = requests.get(url=url, params=payload)
# print(respons.json())
# print(respons.url)
