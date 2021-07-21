import requests
import json

def acvalues(cookies, device):
    url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
    payload = {}
    headers = {
        'Cookie': 'JSESSIONID='+cookies
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    x1 = response.text
    x2 = json.loads(x1)
    mode = x2[device]['deviceStatus']['deviceStatus']['mode']
    fan = x2[device]['deviceStatus']['deviceStatus']['fan']
    envTemp = x2[device]['deviceStatus']['deviceStatus']['envTemp']
    envTempShow = x2[device]['deviceStatus']['deviceStatus']['envTempShow']
    tgtTemp = x2[device]['deviceStatus']['deviceStatus']['tgtTemp']
    onoff = x2[device]['deviceStatus']['deviceStatus']['onoff']
    return mode, fan, envTemp, envTempShow, tgtTemp, onoff

def myagenttake(aitarget, macadd, cookies):
    url = "https://www.activate-ac.com/control/turnOnDevices?mac="+macadd+"&rt=30&tmp=" + str(aitarget) + "&mode=Cold&fan=1" 
    payload = {}
    headers = {
    'Cookie': 'JSESSIONID='+cookies
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return response









