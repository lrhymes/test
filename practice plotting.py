# import socket
# import time
import matplotlib.pyplot as plt
from numpy import linspace, sin
import struct
# import serial
# import math

def P():
    plt.pause(0.1)


x = linspace(2.0, 25.0, num=100)
y = sin(x)
fig, (ax,ax1) = plt.subplots(1,2)
line1, = ax.plot(x,y)

plt.pause(0.1)


# figure, (ax,ax2) = plt.subplots(1,2,figsize=(20, 8))
# figure2, xx = plt.subplots(figsize=(10,25))
# line1, = ax.plot(x,y)
# line2, = ax2.plot(x,y)
# plt.pause(0.1)
