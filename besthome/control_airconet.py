import requests

url = "https://www.activate-ac.com/dev/by/pm?mac=40F520381266" # get power meter link to device วัดศรี

payload = {}
headers = {
    'Cookie': 'JSESSIONID=node0v20qal2a1mlanau5oxhz8wr85932.node0'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(response.text)