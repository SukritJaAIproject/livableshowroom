import requests
import json

def acvalues():
    url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
    payload = {}
    headers = {
        # 'Cookie': 'JSESSIONID=node0wos5fa4y5gvs47jcb9198e251124.node0'
        'Cookie': 'JSESSIONID=node0v20qal2a1mlanau5oxhz8wr85932.node0' #PBase
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    x1 = response.text
    x2 = json.loads(x1)
    mode = x2[1]['deviceStatus']['deviceStatus']['mode']
    fan = x2[1]['deviceStatus']['deviceStatus']['fan']
    envTemp = x2[1]['deviceStatus']['deviceStatus']['envTemp']
    envTempShow = x2[1]['deviceStatus']['deviceStatus']['envTempShow']
    tgtTemp = x2[1]['deviceStatus']['deviceStatus']['tgtTemp']
    onoff = x2[1]['deviceStatus']['deviceStatus']['onoff']
    return mode, fan, envTemp, envTempShow, tgtTemp, onoff

def myagenttake(aitarget):
    # url = "https://www.activate-ac.com/control/turnOnDevices?mac=C82B962C7F5C&rt=30&tmp="+str(aitarget)+"&mode=Cold&fan=1"
    url = "https://www.activate-ac.com/control/turnOnDevices?mac=40F520381E9C&rt=30&tmp=" + str(aitarget) + "&mode=Cold&fan=1" #PBase
    payload = {}
    headers = {
        # 'Cookie': 'JSESSIONID=node0wos5fa4y5gvs47jcb9198e251124.node0'
        'Cookie': 'JSESSIONID=node0v20qal2a1mlanau5oxhz8wr85932.node0' #PBase
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return response









