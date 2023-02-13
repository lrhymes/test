import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import struct
import serial 


X = np.linspace(0,9,10)
Y = np.zeros(10)+14000
# #exec(open("main.py").read())
# 

figure, ax = plt.subplots(figsize=(10, 8))
line, = ax.plot(Y)

    

# 
ii = 0


s = serial.Serial("/dev/ttyACM0",9600)
s.flush()

while True:
    s.flush()
    data = s.read(4)
    temp, = struct.unpack('>I', data)
    print(temp)
    print(list(data))
    ii = ii + 1
    i = ii%10
    
    #Y[0:9] = Y[1:10]
    #Y[9] = temp[0]
    Y = np.append(Y,temp)
    line.remove()
    line, = ax.plot(Y)
    ax.axis([-2, np.size(Y), min(Y)-2, max(Y)+2])
    
    plt.pause(0.1)

