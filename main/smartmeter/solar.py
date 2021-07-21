# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime
# from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP
#
# latitude, longitude, tz = 15.13, 101.52, 'Asia/Jakarta'
# start = pd.Timestamp(datetime.date.today(), tz=tz)
# end = start + pd.Timedelta(days=7)
# irrad_vars = ['ghi', 'dni', 'dhi']
# model = GFS()
# raw_data = model.get_data(latitude, longitude, start, end)
# print('raw_data', raw_data)

import json
import requests
import time
from helper_function.thingb import *
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP

latitude, longitude, tz = 15.13, 101.52, 'Asia/Jakarta'
THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = '2S3XhvVfubWjU7XxGA8p'

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

while True:
    start = pd.Timestamp(datetime.date.today(), tz=tz)
    end = start + pd.Timedelta(days=7)
    irrad_vars = ['ghi', 'dni', 'dhi']
    model = GFS()
    data = model.get_processed_data(latitude, longitude, start, end)

    payload = "{"
    payload += "\"temp_air\":" + str(data['temp_air']) + ",";
    payload += "\"wind_speed\":" + str(data['wind_speed']) + ",";
    payload += "\"ghi\":" + str(data['ghi']) + ",";
    payload += "\"dni\":" + str(data['dni']) + ",";
    payload += "\"dhi\":" + str(data['dhi']) + ",";
    payload += "\"total_clouds\":" + str(data['total_clouds']) + ",";
    payload += "\"low_clouds\":" + str(data['low_clouds']) + ",";
    payload += "\"mid_clouds\":" + str(data['mid_clouds']) + ",";
    payload += "\"high_clouds\":" + str(data['high_clouds']);
    payload += "}"
    client.publish('v1/devices/me/telemetry', payload, 1)
    print('payload =', payload)
    time.sleep(60)

client.loop_stop()
client.disconnect()