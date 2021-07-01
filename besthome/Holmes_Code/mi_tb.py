import time
import paho.mqtt.client as mqtt
import json
from miio import Gateway

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'tQlxqQkPIFyCyAxzD0M4'
INTERVAL=60*15

next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

gateway = Gateway("192.168.1.55", "776332343455735a6d4a73746b48694f")
gateway.discover_devices()
devices = gateway.devices

for dev in devices.values():
    dev.update()
    print(dev)

lumi1 = devices['lumi.158d00069384bf']
lumi2 = devices['lumi.158d0006b1ce02']
print(lumi1.status['temperature'])

try:
    while True:
        payload = "{"
        payload += "\"mi_temp1\":" + str(lumi1.status['temperature']) + ",";
        payload += "\"mi_rh1\":" + str(lumi1.status['humidity']) + ",";
        payload += "\"mi_press1\":" + str(lumi1.status['pressure']) + ",";
        payload += "\"mi_temp2\":" + str(lumi2.status['temperature']) + ",";
        payload += "\"mi_rh2\":" + str(lumi2.status['humidity']) + ",";
        payload += "\"mi_press2\":" + str(lumi2.status['pressure']);
        payload += "}"
        print(payload)
        print(json.dumps(payload))
        client.publish('v1/devices/me/telemetry', payload, 1)
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()