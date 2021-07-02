from miio import Gateway

gateway = Gateway("192.168.1.41", "4f3330576b7978614663343033454231")

gateway.discover_devices()
devices = gateway.devices

for dev in devices.values():
    dev.update()
    print(dev)