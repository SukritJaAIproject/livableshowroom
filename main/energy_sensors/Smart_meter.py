import tinytuya
# d = tinytuya.OutletDevice('eb20777ea024cd6513xszn', '192.168.1.56', '136505aacd17c31b')
# d = tinytuya.OutletDevice('eb1ceaa5d614f75210npxo', '192.168.1.12', 'e35ffceae9df54bd')
d = tinytuya.OutletDevice('eb20777ea024cd6513xszn', '192.168.1.14', 'a6630cd69ffebe12')
d.set_version(3.3)
data = d.status()
print('set_status() result %r' % data)

# Access ID/Client ID: YOUR_TUYA_CLIENT_ID
# Access Secret/Client Secret: YOUR_SECRET_KEY

