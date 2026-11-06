from miio import Gateway

gateway = Gateway("192.168.1.41", "YOUR_SECRET_KEY",lazy_discover=True, start_id=1000)

gateway.discover_devices()
devices = gateway.devices

for dev in devices.values():
    dev.update()
    print(dev)

lumi1 = devices['lumi.158d0006b1ce02']
print(lumi1.status)
print(lumi1.status['temperature'])
print(lumi1.status['humidity'])
print(lumi1.status['pressure'])

lumi2 = devices['lumi.158d0006b1ce02']
print(lumi2.status)
print(lumi2.status['temperature'])
print(lumi2.status['humidity'])
print(lumi2.status['pressure'])
