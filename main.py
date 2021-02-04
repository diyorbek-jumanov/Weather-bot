import requests
import os
import pprint

key = os.environ['key']
token = os.environ['token']

def Updates():
    url_update = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_u = requests.get(url=url_update)
    data = respons_u.json()['result']
    last_msg = data[-1]

    return last_msg


def Weather(text):
    payload = {
        'appid': key,
        'q': text
    }
    url_w = f'https://api.openweathermap.org/data/2.5/weather'
    respons_w = requests.get(url=url_w, params=payload)
    data_w = respons_w.json()





msg_id = Updates()['message']['message_id']

while True:
    data = Updates()
    last_msg_id = data['message']['message_id']
    msg_text = data['message']['text']

    if msg_id != last_msg_id:
        weather_data = Weather(msg_text)


