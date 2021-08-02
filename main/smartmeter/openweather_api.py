import time
import paho.mqtt.client as mqtt
import json
import requests

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'JLeN19Z3YxwxJsDNBfcd'

api_key = "c8a441c6520d8a263990810629ac5c70"
lat = "13.8116043"
lon = "100.368037"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=60*13

# sensor_data = {'temperature': 0, 'humidity': 0}
next_reading = time.time()
client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:

        response = requests.get(url)
        data = json.loads(response.text)
        # print('data', data)
        temp = data['current']['temp']
        feels_like = data['current']['feels_like']
        humidity = data['current']['humidity']
        dew_point = data['current']['dew_point']
        clouds = data['current']['clouds']
        uvi = data['current']['uvi']
        wind_speed = data['current']['wind_speed']
        payload = "{"
        payload += "\"temp\":" + str(temp) + ",";
        payload += "\"feels_like\":" + str(feels_like) + ",";
        payload += "\"humidity\":" + str(humidity) + ",";
        payload += "\"dew_point\":" + str(dew_point) + ",";
        payload += "\"clouds\":" + str(clouds) + ",";
        payload += "\"uvi\":" + str(uvi) + ",";
        payload += "\"wind_speed\":" + str(wind_speed);
        payload += "}"
        print(payload)
        print(json.dumps(payload))

        # client.publish('v1/devices/me/telemetry', json.dumps(payload), 1)
        client.publish('v1/devices/me/telemetry', payload, 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()