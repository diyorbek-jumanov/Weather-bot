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

    full_data_w = list()
    full_data_w.append(data_w['name'])
    full_data_w.append(data_w['main']['temp'] - 273)
    full_data_w.append(data_w['weather']['description'])
    full_data_w.append(data_w['weather']['icon'])
    full_data_w.append(data_w['wind']['speed'])

    return full_data_w




msg_id = Updates()['message']['message_id']

while True:
    data = Updates()
    last_msg_id = data['message']['message_id']
    msg_text = data['message']['text']

    if msg_id != last_msg_id:
        w_d = Weather(msg_text)
        w_from = w_d[0]
        w_temp = w_d[1]
        w_description = w_d[2]
        w_icon = w_d[3]
        w_w = w_d[4]
        
        send_msg_text = f"from: {w_from}\nTemp: {w_temp} {w_icon}\ndescription: {w_description}\nWind: {w_w}"

        



