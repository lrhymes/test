import serial
import matplotlib.pyplot as plt
import numpy as np
import struct
import p
import array
from NTCLE100E3103JB0 import *
import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('QtAgg')
#matplotlib.use('GTK4Agg')
#matplotlib.use('WXAgg')

s = serial.Serial()
try:
    s.port='/dev/ttyACM0'
    s.open()
except:
    s.port='/dev/ttyACM1'
    s.open()



N = 256

fig,ax = plt.subplots()
y = np.zeros(N*2)
line, = ax.plot(y,'-b')
line2, = ax.plot(y,':')
ax.set_ylim([-.5,4])
plt.grid(True)
ax.grid(which='major', linestyle='-', linewidth='1', color='black')
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

i = 0
fr = 1000
F = struct.pack("!I", fr)

while True:
    i = i + 1
    #nwait = s.in_waiting
    s.flushInput()
    s.write(b'150000')
    s.write(b'\n')
    n = s.read(N*4)
    n = np.array(array.array("I",n))
    #n, = struct.unpack("<I",s.read(4))
    n = n*3.3/65536
    y = np.append(y[len(n):len(y)],[n])
    #yy = y[len(y)-300:len(y)]
    #xx = np.arange(1,len(y)+0.0001,1)
    #line, = ax.plot(xx,y,'-b')
    if(i%1 == 0):
        line.set_ydata(y)
        tmean = np.mean(y[len(y)-N:len(y)])
        ax.set_title('%.5f' % tmean ,fontsize=40)
        t3 = np.ones(N*2)*tmean
        line2.set_ydata(t3)
        
        
        plt.pause(0.00001)
        nwait2 = s.in_waiting

