# Authorization key obtained from the cloud development project
client_id = 'ypgeygnjapkvce6p3uwb'
secret = 'a5e85bedb96141e5846d0a04d4fba10d'

# Call the APIs according to your region.
# China https://openapi.tuyacn.com
# America https://openapi.tuyaus.com
# Europe https://openapi.tuyaeu.com
# India https://openapi.tuyain.com

base = 'https://openapi.tuyaus.com'

# Signature algorithm function
def calc_sign(msg,key):
  import hmac
  import hashlib

  sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
  return sign

import json
# get request function
def GET(url, headers={}):

  t = str(int(time.time()*1000))
  default_par={
      'client_id':client_id,
      'access_token':res['access_token'],
      'sign':calc_sign(client_id+res['access_token']+t, secret),
      't':t,
      'sign_method':'HMAC-SHA256',
      }
  r = requests.get(base + url, headers=dict(default_par,**headers))

  r = json.dumps(r.json(), indent=2, ensure_ascii=False) # Beautify the format of request result.
  return r

# post request function
def POST(url, headers={}, body={}):
  import json
  t = str(int(time.time()*1000))

  default_par={
      'client_id':client_id,
      'access_token':res['access_token'],
      'sign':calc_sign(client_id+res['access_token']+t, secret),
      't':t,
      'sign_method':'HMAC-SHA256',
      }
  r = requests.post(base + url, headers=dict(default_par,**headers), data=json.dumps(body))

  r = json.dumps(r.json(), indent=2, ensure_ascii=False) # Beautify the format of request result.
  return r

import time
import requests
t = str(int(time.time()*1000))
r = requests.get(base+'/v1.0/token?grant_type=1',
                 headers={
                    'client_id':client_id,
                    'sign':calc_sign(client_id+t, secret),
                    'secret':secret,
                    't':t,
                    'sign_method':'HMAC-SHA256',
                  })

res = r.json()['result']
print('res', res)
print('access_token', res['access_token'])
print('refresh_token', res['refresh_token'])
print('uid', res['uid'])
print('sign', calc_sign(client_id+res['access_token']+t, secret))


# import json
# import requests
#
# headers = {
#     'sign_method': 'HMAC-SHA256',
#     'client_id': 'ypgeygnjapkvce6p3uwb',
#     't': '1625587043921',
#     'mode': 'cors',
#     'Content-Type': 'application/json',
#     # 'sign': '05E1D154D35FD7B4151363CFE9485E4B14D1EE9E88B876A1F0425623BF71139F',
#     'sign': calc_sign(client_id+res['access_token']+t, secret),
#     # 'access_token': 'c381fe456c3fe8002c1aefb93dde52c6',
#     'access_token': res['access_token'],
# }
#
# response = requests.get('https://openapi.tuyaus.com/v1.0/devices/eb1ceaa5d614f75210npxo/status', headers=headers)
#
# data = response.text
# dataj = json.loads(data)
#
# print(dataj)
# print('forward_energy_total = ', dataj['result'][0]['value'])
# print('electricCurrent = ', json.loads(dataj['result'][1]['value'])['electricCurrent'])
# print('power = ', json.loads(dataj['result'][1]['value'])['power'])
# print('voltage = ', json.loads(dataj['result'][1]['value'])['voltage'])

# Linked device's ID in the cloud development project
device_id = 'eb1ceaa5d614f75210npxo'
r = GET(url=f'/v1.0/devices/{device_id}/status')
print(r)
r = json.loads(r)
print('forward_energy_total = ', r['result'][0]['value'])
print('electricCurrent = ', json.loads(r['result'][1]['value'])['electricCurrent'])
print('power = ', json.loads(r['result'][1]['value'])['power'])
print('voltage = ', json.loads(r['result'][1]['value'])['voltage'])

energy_total =  r['result'][0]['value']
electricCurrent =  json.loads(r['result'][1]['value'])['electricCurrent']
power =  json.loads(r['result'][1]['value'])['power']
voltage = json.loads(r['result'][1]['value'])['voltage']


from helper_function.thingb import *
from helper_function.acdata import *
import time

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'ivSOUVEah654Iyxd9HdF'  # AC status

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
    while True:

        payload = "{"
        payload += "\"energy_total\":" + str(energy_total) + ",";
        payload += "\"electricCurrent\":" + str(energy_total) + ",";
        payload += "\"power\":" + str(energy_total) + ",";
        payload += "\"voltage\":" + str(electricCurrent);
        payload += "}"
        client.publish('v1/devices/me/telemetry', payload, 1)
        print('payload =', payload)
        time.sleep(60 * 5)
except:
    print("cant sent")

client.loop_stop()
client.disconnect()