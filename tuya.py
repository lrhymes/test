import tinytuya

deviceID = "ebca25c259c207d9739dco"
ipAddress = "192.168.1.204"
localKey = "f3a13015a2383a21"

f = {'deviceID' : 'ebca25c259c207d9739dco', 'ipAddress' : '192.168.1.204', 'localKey' : 'f3a13015a2383a21' }
#{
#    name: 'ler pwr',
#    id: 'ebca25c259c207d9739dco',
#    key: 'f3a13015a2383a21'
#  }

f = { 'name': 'ler pwr',  'id': 'ebca25c259c207d9739dco',  'key': 'f3a13015a2383a21'  }

d = tinytuya.OutletDevice(dev_id='ebca25c259c207d9739dco',address='192.168.1.204',local_key='f3a13015a2383a21', version=3.3)

                          
data = d.status()

print('Dictionary %r' % data)