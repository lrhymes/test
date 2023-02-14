import serial
import matplotlib.pyplot as plt
import numpy as np
import struct

def sens2temp(iii):
    cf = 3.3/65535.0
    temp = iii * cf
    temC = 27.0 - ( temp - 0.706 )/ 0.001721
    temF = temC * 9.0/5.0 + 32.0
    return temF




s = serial.Serial()
s.port='/dev/ttyACM0'
s.open()

y = np.array([])

fig,ax = plt.subplots()
#p1, = ax.plot(x,np.sin(x))
s.flush()
while True:
    
    ti, = struct.unpack("!I", s.read(4))
    print(ti)
    tti = sens2temp(ti)
    print(tti)
    y = np.append(y,[tti])
    ax.plot(y)
    plt.pause(0.01)






