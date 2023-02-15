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
    return float(iii)




s = serial.Serial()
s.port='/dev/ttyACM0'
s.baudrate = 256000
s.open()

y = np.array([])

fig,ax = plt.subplots()
#l, = ax.plot([])
#p1, = ax.plot(x,np.sin(x))
s.flushInput()
y = np.zeros(100)
line, = ax.plot(y,'-b')
ax.set_ylim([-6,6])
i = 0
while True:
    i = i + 1
    print(s.in_waiting)
    s.flushInput()
    n, = struct.unpack("!I",s.read(4))
    #n = float(n)
  #  n = (n-14000)/16
  #  print(n)
#     s.flush()
#     ti, = struct.unpack("!I", s.read(4))
#     print(ti)
#     tti = sens2temp(ti)
#     print(tti)
    y = np.append(y[1:len(y)],[n])
    #yy = y[len(y)-300:len(y)]
    #xx = np.arange(1,len(y)+0.0001,1)
    #line, = ax.plot(xx,y,'-b')
    if(i%7 == 0):
        line.set_ydata(y)
        ax.set_ylim([min(y)-4, max(y)+4])
        plt.pause(0.00001)
    #l.set_ydata(yy)
    #l.set_xdata(xx)
    #plt.show()
   # ax.set_ylim([min(y)-4, max(y)+4])
   # plt.pause(0.001)
    #line.remove()







