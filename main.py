import requests
import os
import pprint

key = os.environ['key']
token = os.environ['token']

payload = {
    'appid': key,
    'q': 'Samarqand'
}
url = f'https://api.openweathermap.org/data/2.5/weather'
respons = requests.get(url=url, params=payload)
print(respons.json())
print(respons.url)
