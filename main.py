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
    print(respons_w.url)
    # pprint(data_w)
    eror = data_w.get('message')
    if eror == None:
        full_data_w = list()
        full_data_w.append(data_w['name'])
        full_data_w.append(data_w['main']['temp'] - 273)
        full_data_w.append(data_w['weather'][0]['description'])
        full_data_w.append(data_w['weather'][0]['icon'])
        full_data_w.append(data_w['wind']['speed'])

        return full_data_w
    
    return "Bunday shahar mavjud emas!"


def SendMessage(ch_id, m_text):
    url_send = f'https://api.telegram.org/bot{token}/sendMessage'
    payl = {
        'chat_id': ch_id,
        'text': m_text
    }
    respons_s = requests.get(url=url_send, params=payl)
    

msg_id = Updates()['message']['message_id']

while True:
    data = Updates()
    last_msg_id = data['message']['message_id']
    
    if msg_id != last_msg_id:
        msg_text = data['message']['text'].title()
        chat_id = data['message']['from']['id']

        w_d = Weather(msg_text)
        if "Bunday shahar mavjud emas!" not in w_d:
            w_from = w_d[0]
            w_temp = w_d[1]
            w_description = w_d[2]
            w_icon = w_d[3]
            w_w = w_d[4]
            
            send_msg_text = f"from: {w_from}\nTemp: {round(w_temp, 2)} {w_icon}\ndescription: {w_description}\nWind: {w_w} m/s"

            SendMessage(chat_id, send_msg_text)
        else:
            SendMessage(chat_id, w_d)

        msg_id = last_msg_id
