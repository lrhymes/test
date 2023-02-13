import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import struct
import serial 


plt.axis([-1, 11, -0.2, 1.2])
X = np.linspace(0,9,10)
Y = np.zeros(10)
# #exec(open("main.py").read())
# 
plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(X, Y)

# 
figure2, ax2 = plt.subplots(figsize=(10, 8))
line2, = ax2.plot(X, Y)

# 
ii = 0


s = serial.Serial("/dev/ttyACM0",9600)
s.flush()

while True:
    s.flush()
    data = s.read(4)
    temp = struct.unpack('<I', data)
    print(temp)
    print(list(data))
    ii = ii + 1
    i = ii%10
    
    Y[0:9] = Y[1:10]
    Y[9] = temp[0]
    
    line1.set_xdata(X)
    line1.set_ydata(Y)
    line2.set_ydata(np.flip(Y))
    
    ax.axis([-2, 12, min(Y)-2, max(Y)+2])
    ax2.axis([-2, 12, min(Y)-2, max(Y)+2])
    
    figure.canvas.draw()
    figure.canvas.flush_events()
    figure2.canvas.draw()
    figure2.canvas.flush_events()
 
    time.sleep(0.01)

