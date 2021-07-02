from pythermalcomfort.models import pmv_ppd
from pythermalcomfort.psychrometrics import v_relative
from pythermalcomfort.utilities import met_typical_tasks
from pythermalcomfort.utilities import clo_typical_ensembles
from helper_function.thingb import *
from helper_function.acdata import *
import time

# print(acvalues('node0rn5sn3feu38d5rbgx853kmgc3181.node0', 0))
# print(myagenttake(25, 'C82B962C7F5C', 'node0rn5sn3feu38d5rbgx853kmgc3181.node0'))

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'gAmeVYhTTyVdMuYcXVMc'  # AC status

v = 0.1
met = met_typical_tasks["Writing"]
icl = clo_typical_ensembles["Trousers, long-sleeve shirt"]
vr = v_relative(v=v, met=met)

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
    while True:
        _, _, _, _, tgtTemp, _ = acvalues('node0rn5sn3feu38d5rbgx853kmgc3181.node0', 0)
        T_indoor = float(getdatatb('d8806410-8c4f-11eb-b31a-8f46a0a92737/values/timeseries?keys=T_DHT22')['T_DHT22'][0]['value'])
        rh_indoor = float(getdatatb('d8806410-8c4f-11eb-b31a-8f46a0a92737/values/timeseries?keys=Rh_DHT22')['Rh_DHT22'][0]['value'])
        PMV = pmv_ppd(tdb=T_indoor, tr=T_indoor, vr=vr, rh=rh_indoor, met=met, clo=icl, standard="ASHRAE")['pmv']
        payload = "{"
        payload += "\"pmv\":" + str(PMV) + ",";
        payload += "\"tgtTemp\":" + str(tgtTemp);
        payload += "}"
        client.publish('v1/devices/me/telemetry', payload, 1)
        print('payload =', payload)
        time.sleep(60 * 5)
except:
    print("cant sent")

client.loop_stop()
client.disconnect()