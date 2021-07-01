# import requests
# import json
#
# url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
# payload = {}
# headers = {
#     'Cookie': 'JSESSIONID=node096zpn8553rfp19bzyycalj0km4875.node0'
# }
# response = requests.request("GET", url, headers=headers, data=payload, verify=False)
# x1 = response.text
# x2 = json.loads(x1)
# print('x2', x2)

import requests
import json
import datetime
import pandas as pd

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

# 2021-04-28,00:00','2021-04-28,17:00'  = 1619542860000, 1619604060000
# 2021-05-01,00:00','2021-05-01,08:00' = 1619802060000, 1619830860000
# 2021-05-02,10:00','2021-05-02,17:00' = 1619924460000, 1619949660000

# url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/timeseries?limit=900000&keys=ACP1&startTs=1619542860000&endTs=1619604060000"
# url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/timeseries?limit=900000&keys=ACP1&startTs=1619802060000&endTs=1619830860000"
# url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/timeseries?limit=900000&keys=ACP1&startTs=1619924460000&endTs=1619949660000"
# url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/timeseries?limit=900000&keys=ACP1&startTs=1619740860000&endTs=1619767800000"
# url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/timeseries?limit=900000&keys=ACP1&startTs=1620482400000&endTs=1620433800000"

# วันที่ 7/5/2564 เวลา 21.00 - 8/5/2564 เวลา 07.30 น.       1620396000000 -> 1620433800000
# วันที่ 9/5/2564 เวลา 20.40 - 10/5/2564 เวลา 07.10 น.      1620567600000 -> 1620605400000
# วันที่ 9/5/2564 เวลา 12.40 - 16.20 น.                    1620538800000 -> 1620552000000
# วันที่ 10/5/2564 เวลา 13.20 - 17.00 น                    1620627600000 -> 1620640800000
# วันที่ 8/5/2564 เวลา 21.00 - 8/5/2564 เวลา 07.30 น.       1620482400000 -> 1620520200000


url = "https://things.egat.co.th/api/plugins/telemetry/DEVICE/8e096a20-981c-11eb-b31a-8f46a0a92737/values/" \
      "timeseries?limit=900000&keys=ACP1&" \
      "startTs=1620482400000&" \
      "endTs=1620520200000"

payload = {}
headers = {'X-Authorization': tokendata()}
print('headers', headers)
response = requests.request("GET", url, headers=headers, data=payload)
print('response', response.text)
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
# print(datedf.head())
# print(listvaldf.head())

result = pd.concat([datedf, listvaldf], axis=1, join="inner")
print(result.head())
# result.to_csv('1619542860000_to_1619604060000_power.csv')
# result.to_csv('1619802060000_to_1619830860000_power.csv')
# result.to_csv('1619924460000_to_1619949660000power.csv')
result.to_csv('1620482400000_1620433800000.csv')