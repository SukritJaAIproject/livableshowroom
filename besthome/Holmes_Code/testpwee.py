

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
