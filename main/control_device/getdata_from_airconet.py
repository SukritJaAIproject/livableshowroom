import requests
import json

url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
payload = {}
headers = {
    'Cookie': 'JSESSIONID=node0rn5sn3feu38d5rbgx853kmgc3181.node0'
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
print(mode, fan, envTemp, envTempShow, tgtTemp, onoff)


'''
import requests
import json

url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
payload = {}
headers = {
    'Cookie': 'JSESSIONID=node0rn5sn3feu38d5rbgx853kmgc3181.node0'
}
response = requests.request("GET", url, headers=headers, data=payload, verify=False)
x1 = response.text
x2 = json.loads(x1)
print('x2', x2)
'''