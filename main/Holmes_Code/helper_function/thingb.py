import requests
import json
import paho.mqtt.client as mqtt

def tokendata():
    BASE_URL = 'https://things.egat.co.th'
    USERNAME = 'sukrit.jai@egat.co.th'
    PASSWORD = 'Sj@scg19'

    headers = {'Content-Type': 'application/json','Accept': 'application/json'}
    data = '{"username":"'+ USERNAME + '", "password":"' + PASSWORD + '"}'
    tokenDict = requests.post(BASE_URL+'/api/auth/login', headers=headers, data=data).json()

    TBAPI_TOKEN_KEY = tokenDict['token']
    session = requests.Session()
    session.headers = {'Content-Type': 'application/json','X-Authorization': '',}
    session.headers['X-Authorization'] = str('Bearer ' + TBAPI_TOKEN_KEY)
    token_m = session.headers['X-Authorization']
    return token_m

def getdatatb(urldevice):

    # urldevice = "d8806410-8c4f-11eb-b31a-8f46a0a92737/values/timeseries?keys=humidity"
    urlstr = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/"
    url = urlstr + urldevice

    payload = {}
    headers = {'X-Authorization': tokendata()}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)


