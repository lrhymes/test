import serial
import matplotlib.pyplot as plt
import numpy as np
import struct
import p
from NTCLE100E3103JB0 import *

def sens2temp(iii):
    cf = 3.3/65535.0
    temp = iii * cf
    temC = 27.0 - ( temp - 0.706 )/ 0.001721
    temF = temC * 9.0/5.0 + 32.0
    return float(iii)


 
A = -14.6337
B = 4791.842
C = -115334
D = -3.730535E+06

#Tolerances = 3.354016E-03 2.569850E-04 2.620131E-06 6.383091E-08

s = serial.Serial()
s.port='/dev/ttyACM0'
s.baudrate = 256000
s.open()

y = np.array([])

fig,ax = plt.subplots()
#l, = ax.plot([])
#p1, = ax.plot(x,np.sin(x))
s.flushInput()
y = np.zeros(1000)
line, = ax.plot(y,'-b')
ax.set_ylim([0,3.3])

fig2,ax2 = plt.subplots()
y2 = np.zeros(1000)
line2, = ax2.plot(y2,'-b')
ax2.set_ylim([60,90])

i = 0
while True:
    i = i + 1
    nwait = s.in_waiting
    s.flushInput()
    n, = struct.unpack("!I",s.read(4))
    n = float(n)*3.3/65536
    #n  = 1000/(1000+r)*3.3
    r = 1/(n/(3.3*1000))-1000
    r = r2t(r)-273.15
    r = 9/5*r + 32
  #  n = (n-14000)/16
#     s.flush()
#     ti, = struct.unpack("!I", s.read(4))
#     print(ti)
#     tti = sens2temp(ti)
#     print(tti)
    y = np.append(y[1:len(y)],[n])
    y2 = np.append(y2[1:len(y2)],[r])
    #yy = y[len(y)-300:len(y)]
    #xx = np.arange(1,len(y)+0.0001,1)
    #line, = ax.plot(xx,y,'-b')
    if(i%10 == 0):
        line.set_ydata(y)
        line2.set_ydata(y2)
        #ax.set_ylim([min(y)-4, max(y)+4])
        #s.flushInput()
        plt.pause(0.00001)
        nwait2 = s.in_waiting
        s.flushInput()
   # if(i%50 == 0 ):
        #ax.set_ylim([min(y)-10, max(y)+10])
      #  plt.pause(0.00001)
      #  s.flushInput()
    #l.set_ydata(yy)
    #l.set_xdata(xx)
    #plt.show()
   # ax.set_ylim([min(y)-4, max(y)+4])
   # plt.pause(0.001)
    #line.remove()







