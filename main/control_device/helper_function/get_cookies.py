import requests
from requests.auth import HTTPBasicAuth
def getcookie():
    s = requests.Session()
    s.post('https://www.activate-ac.com/user/login', auth=('YOUR_EMAIL', 'YOUR_PASSWORD'), verify=False)
    return s.cookies.items()[0][1]


#
# s = requests.Session()
# s.post('https://www.activate-ac.com/user/login', auth=('YOUR_EMAIL', 'YOUR_PASSWORD'), verify=False)
# print(s.cookies)
# print(s.cookies.items()[0][1])
