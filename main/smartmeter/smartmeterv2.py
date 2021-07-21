import json
import requests
from helper_function.thingb import *
from helper_function.acdata import *
import time

client_id = 'ypgeygnjapkvce6p3uwb'
secret = 'a5e85bedb96141e5846d0a04d4fba10d'
base = 'https://openapi.tuyaus.com'
device_id = 'eb20777ea024cd6513xszn'

def calc_sign(msg,key):
  import hmac
  import hashlib
  sign = hmac.new(msg=bytes(msg, 'latin-1'),key = bytes(key, 'latin-1'), digestmod = hashlib.sha256).hexdigest().upper()
  return sign

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

def POST(url, headers={}, body={}):
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

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'ivSOUVEah654Iyxd9HdF'  # AC status

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
    while True:
        t = str(int(time.time() * 1000))
        r = requests.get(base + '/v1.0/token?grant_type=1',
                         headers={'client_id': client_id, 'sign': calc_sign(client_id + t, secret),
                                  'secret': secret, 't': t, 'sign_method': 'HMAC-SHA256', })
        res = r.json()['result']
        r = GET(url=f'/v1.0/devices/{device_id}/status')
        # print(r)
        r = json.loads(r)
        energy_total = r['result'][0]['value']
        electricCurrent = json.loads(r['result'][1]['value'])['electricCurrent']
        power = json.loads(r['result'][1]['value'])['power']
        voltage = json.loads(r['result'][1]['value'])['voltage']

        payload = "{"
        payload += "\"energy_total2\":" + str(energy_total) + ",";
        payload += "\"electricCurrent2\":" + str(electricCurrent) + ",";
        payload += "\"power2\":" + str(power) + ",";
        payload += "\"voltage2\":" + str(voltage);
        payload += "}"
        client.publish('v1/devices/me/telemetry', payload, 1)
        print('payload =', payload)
        time.sleep(60)
except:
    print("cant sent")

client.loop_stop()
client.disconnect()