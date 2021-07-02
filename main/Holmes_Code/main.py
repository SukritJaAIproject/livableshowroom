from helper_function.get_cookies import *
from helper_function.calpmv import *
from helper_function.thingb import *
from helper_function.holmes_agent import *
from tensorflow.keras.optimizers import Adam
from helper_function.acdata import *
import time

THINGSBOARD_HOST = 'mqtt.egat.co.th'
ACCESS_TOKEN = 'gAmeVYhTTyVdMuYcXVMc'  # AC status

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

model = build_model(states, actions)
dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-4), metrics=['mae'])
dqn.load_weights(r'C:\Users\sukri\PycharmProjects\Holmes_Code\model\Holmes_2564_04_27_intv2_change_reward.h5f')

while True:
    mode, fan, envTemp, envTempShow, tgtTemp, onoff = acvalues()
    outdoor = getdatatb('4b156b90-903a-11eb-b31a-8f46a0a92737/values/timeseries?keys=T_DHT22')['T_DHT22'][0]['value']
    rh_indoor = float(getdatatb('d8806410-8c4f-11eb-b31a-8f46a0a92737/values/timeseries?keys=Rh_DHT22')['Rh_DHT22'][0]['value'])
    T_indoor = float(getdatatb('d8806410-8c4f-11eb-b31a-8f46a0a92737/values/timeseries?keys=T_DHT22')['T_DHT22'][0]['value'])
    print('inT_DHT = ', T_indoor,'  ','inTempAirConet', envTemp)
    pmv = calpmv(T_indoor, rh_indoor)
    state_T = np.array([tgtTemp,T_indoor,outdoor,pmv,0]).reshape(1, -1)
    action_T = np.argmax(dqn.compute_q_values(state_T))
    aitarget = tgtTemp + (action_T-1)
    com = myagenttake(aitarget)
    print('oldtemp', tgtTemp)
    print('Turn =', convertdic(action_T))
    _, _, _, _, tgtTemp,_ = acvalues()
    print('tgtTemp =', tgtTemp)

    try:
        payload = "{"
        payload += "\"mode\":" + str(mode) + ",";
        payload += "\"fan\":" + str(fan) + ",";
        payload += "\"envTemp\":" + str(envTemp) + ",";
        payload += "\"envTempShow\":" + str(envTempShow) + ",";
        payload += "\"pmv\":" + str(pmv) + ",";
        payload += "\"onoff\":" + str(onoff) + ",";
        payload += "\"tgtTemp\":" + str(tgtTemp);
        payload += "}"
        client.publish('v1/devices/me/telemetry', payload, 1)
        print('payload', payload)
        time.sleep(60)
    except:
        print("cant sent")
    time.sleep(60 * 14)

client.loop_stop()
client.disconnect()