import serial
import matplotlib.pyplot as plt
import numpy as np
import struct
import p

def sens2temp(iii):
    cf = 3.3/65535.0
    temp = iii * cf
    temC = 27.0 - ( temp - 0.706 )/ 0.001721
    temF = temC * 9.0/5.0 + 32.0
    return temF




s = serial.Serial()
s.port='/dev/ttyACM0'
s.baudrate = 115200
s.open()

y = np.array([])

fig,ax = plt.subplots()
#l, = ax.plot([])
#p1, = ax.plot(x,np.sin(x))
s.flush()
while True:
    ti, = struct.unpack("!I", s.read(4))
    print(ti)
    tti = sens2temp(ti)
    print(tti)
    y = np.append(y,[tti])
    yy = y[len(y)-300:len(y)]
    xx = np.arange(1,len(yy)+0.0001,1)
    line, = ax.plot(xx,yy,'-b')
    #l.set_ydata(yy)
    #l.set_xdata(xx)
    #plt.show()
    plt.pause(0.000001)
    line.remove()






