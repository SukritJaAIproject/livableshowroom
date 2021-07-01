import requests
from requests.auth import HTTPBasicAuth
def getcookie():
    s = requests.Session()
    s.post('https://www.activate-ac.com/user/login', auth=('6170306321@alumni.chula.ac.th', 'Sj@scg19'), verify=False)
    return s.cookies.items()[0][1]


#
# s = requests.Session()
# s.post('https://www.activate-ac.com/user/login', auth=('6170306321@alumni.chula.ac.th', 'Sj@scg19'), verify=False)
# print(s.cookies)
# print(s.cookies.items()[0][1])