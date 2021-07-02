import requests
import json
import pandas as pd
import datetime

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

url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/" \
      "timeseries?limit=900000&keys=ACP1&" \
      "startTs=1620482400000&" \
      "endTs=1620520200000"

payload = {}
headers = {'X-Authorization': tokendata()}
response = requests.request("GET", url, headers=headers, data=payload)
b = json.loads(response.text)['ACP1']
listval = []
datelist = []

for i in range(len(b)):
    val_m = b[i]['value']
    date_m = datetime.datetime.fromtimestamp(b[i]['ts']/1000.0).strftime('%Y-%m-%d %H:%M:%S')
    listval.append(val_m)
    datelist.append(date_m)
datedf = pd.DataFrame(datelist,columns=['datetimess'])
listvaldf = pd.DataFrame(listval,columns=['values'])

result = pd.concat([datedf, listvaldf], axis=1, join="inner")
print(result.head())