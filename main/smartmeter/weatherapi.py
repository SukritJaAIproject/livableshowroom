import requests
import paho.mqtt.client as paho
import json
import time


ACCESS_TOKEN = 'YY1PzzravgsxTNm1g3x9'  # Token of your device
broker = "mqtt.egat.co.th"  # host name
port = 1883  # data listening port


def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection


url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
querystring = {"lat":"13.4300818","lng":"100.2467665"}
headers = {
    'x-api-key': "iqIH5Z5TiqaVKIZGuvCtn24e7l7ot4naP9mzLoMb",
    'Content-type': "application/json"
    }


while True:

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = json.loads(response.text)
    temp_api = res['data']['temperature']
    humi_api = res['data']['humidity']
    winSp_api = res['data']['windSpeed']
    cloudCover_api = res['data']['cloudCover']

    print('temp_api', temp_api)
    print('humi_api', humi_api)
    print('windSpeed', winSp_api)
    print('cloudCover_api', cloudCover_api)

    payload = "{"
    # payload += "\"temperature\":60,";
    payload += "\"temp_api\":"+ str(temp_api)+",";
    payload += "\"humi_api\":" + str(humi_api) + ",";
    payload += "\"windSpeed\":" + str(winSp_api) + ",";
    payload += "\"cloudCover_api\":" + str(cloudCover_api);
    # payload += "\"Temperature\":25";
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(900)