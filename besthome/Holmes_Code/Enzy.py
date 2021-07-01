import requests
import json
from datetime import datetime
import time

urlenzy = "https://sedp-gw.egat.co.th/api/commontemp"

api_key = "c8a441c6520d8a263990810629ac5c70"
lat = "13.4300818"
lon = "100.2467665"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
INTERVAL=60*2
next_reading = time.time()

while True:
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    response = requests.get(url)
    data = json.loads(response.text)
    temp = data['current']['temp']
    humidity = data['current']['humidity']

    ################### Enzy
    payload = json.dumps([
      {
        "ts": dt_string,
        "site": "s0004",
        "group": "air_iot",
        "item": "temp",
        "value": str(temp)
      },
      {
        "ts": dt_string,
        "site": "s0004",
        "group": "air_iot",
        "item": "Rh",
        "value": str(humidity)
      }
    ])

    print('A', payload)

    headers = {'Content-Type': 'application/json'}
    response_enzy = requests.request("POST", urlenzy, headers=headers, data=payload)
    print(response_enzy.text)

    next_reading += INTERVAL
    sleep_time = next_reading - time.time()
    if sleep_time > 0:
        time.sleep(sleep_time)