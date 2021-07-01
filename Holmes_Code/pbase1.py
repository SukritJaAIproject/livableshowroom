import requests
import json

def acvalues():
    url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=node0wos5fa4y5gvs47jcb9198e251124.node0'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    x1 = response.text
    x2 = json.loads(x1)
    mode = x2[0]['deviceStatus']['deviceStatus']['mode']
    fan = x2[0]['deviceStatus']['deviceStatus']['fan']
    envTemp = x2[0]['deviceStatus']['deviceStatus']['envTemp']
    envTempShow = x2[0]['deviceStatus']['deviceStatus']['envTempShow']
    tgtTemp = x2[0]['deviceStatus']['deviceStatus']['tgtTemp']
    onoff = x2[0]['deviceStatus']['deviceStatus']['onoff']
    return mode, fan, envTemp, envTempShow, tgtTemp, onoff

def myagenttake(aitarget):
    url = "https://www.activate-ac.com/control/turnOnDevices?mac=C82B962C7F5C&rt=30&tmp="+str(aitarget)+"&mode=Cold&fan=1"
    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=node0wos5fa4y5gvs47jcb9198e251124.node0'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return response









