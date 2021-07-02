import requests

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
    
#print(tokendata())