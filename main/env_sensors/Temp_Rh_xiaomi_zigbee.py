from miio import Gateway

gateway = Gateway("192.168.1.41", "YOUR_SECRET_KEY")

gateway.discover_devices()
devices = gateway.devices

for dev in devices.values():
    dev.update()
    print(dev)

