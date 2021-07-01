import requests
import json

# url = "https://www.activate-ac.com/control/turnOnDevices?mac=40F520381266&rt=30&tmp=" + str(27) + "&mode=Cold&fan=1"
# url = "https://www.activate-ac.com/control/turnOnDevices?mac=40F520381E9C&rt=30&tmp=" + str(27) + "&mode=Cold&fan=1"

# url =  "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
# url = "https://www.activate-ac.com/pm/app/master"

# url = "https://www.activate-ac.com/setpoint/dev?mac=40F520381266" #Get device temperature
# url = "https://www.activate-ac.com/setpoint/dev?mac=40F520381E9C" #Get device temperature
#
url = "https://www.activate-ac.com/dev/by/pm?mac=40F520381266" # get power meter link to device วัดศรี
# url = "https://www.activate-ac.com/dev/by/pm?mac=40F520381E9C" # get power meter link to device living room base

# url = "https://www.activate-ac.com/level3-info/power-meter-electric-parameters/app?acMac=40F520381266"
# url = "https://www.activate-ac.com/level3-info/power-meter-electric-parameters/app?acMac=40F520381E9C"


# url = "https://www.activate-ac.com/control/checkDevicesCurrentStatus/40F520381266"
# url = "https://www.activate-ac.com/control/checkDevicesCurrentStatus/40F520381E9C"


payload = {}
headers = {
    # 'Cookie': 'JSESSIONID=node01i9ub88d0nfiq13evv7jhg38072571.node0'
    'Cookie': 'JSESSIONID=node0v20qal2a1mlanau5oxhz8wr85932.node0'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
print(response.text)

# url = "https://www.activate-ac.com/dev/deviceStatusSetPointCurrentStatus"
# payload = {}
# headers = {
#     # 'Cookie': 'JSESSIONID=node0wos5fa4y5gvs47jcb9198e251124.node0'
#     'Cookie': 'JSESSIONID=node0v20qal2a1mlanau5oxhz8wr85932.node0'  # PBase
# }
#
# response = requests.request("GET", url, headers=headers, data=payload, verify=False)
# x1 = response.text
# x2 = json.loads(x1)
# print('x2', x2)
# print('x2[1]', x2[1])
#
# mode = x2[]['deviceStatus']['deviceStatus']['mode']
# fan = x2[1]['deviceStatus']['deviceStatus']['fan']
# envTemp = x2[1]['deviceStatus']['deviceStatus']['envTemp']
# envTempShow = x2[1]['deviceStatus']['deviceStatus']['envTempShow']
# tgtTemp = x2[1]['deviceStatus']['deviceStatus']['tgtTemp']
# onoff = x2[1]['deviceStatus']['deviceStatus']['onoff']
# print(mode, fan, envTemp, envTempShow, tgtTemp, onoff)

# from miio import Gateway
#
# gateway = Gateway("192.168.2.53", "776466463739795a4c61775161427071")
#
# gateway.discover_devices()
# devices = gateway.devices
#
# for dev in devices:
#     dev.update()
#     print(dev)


# from miio import Gateway
#
# gateway = Gateway("192.168.1.55", "776332343455735a6d4a73746b48694f")
#
# gateway.discover_devices()
# devices = gateway.devices
#
# for dev in devices.values():
#     dev.update()
#     print(dev)

# from miio import Gateway
import time
#
# gateway = Gateway("192.168.1.55", "776332343455735a6d4a73746b48694f")
# gateway = Gateway("192.168.1.55", "776332343455735a6d4a73746b48694f",lazy_discover=True, start_id=1000)
# # gateway = Gateway("119.76.150.235", "b79b9b72497c6dba7ac0a072")
# # print(gateway.get_prop())
#
# gateway.discover_devices()
# devices = gateway.devices
# # print(type(devices))
# # print(devices)
# # print(devices.keys())
#
# for dev in devices.values():
#     dev.update()
#     print(dev)
#
# walloutlet = devices[5]
# print(walloutlet.toggle())

# gateway = Gateway("192.168.1.55", "776332343455735a6d4a73746b48694f")
# gateway.discover_devices()
# devices = gateway.devices
#
# for dev in devices.values():
#     dev.update()
#     print(dev)
#
# lumi1 = devices['lumi.158d00069384bf']
# print(lumi1.status)
# print(lumi1.status['temperature'])
# print(lumi1.status['humidity'])
# print(lumi1.status['pressure'])
#
# print('#############################')
#
# lumi2 = devices['lumi.158d0006b1ce02']
# print(lumi2.status)
# print(lumi2.status['temperature'])
# print(lumi2.status['humidity'])
# print(lumi2.status['pressure'])
# from miio import Vacuum

# miiocli device --ip <ip> --token <token> info
