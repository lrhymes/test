import socket
import time
import matplotlib.pyplot as plt
from numpy import *
import struct
import serial
import math

x = linspace(2.0, 25.0, num=100)
y = sin(x)

plt.ion()

figure, (ax,ax2) = plt.subplots(1,2,figsize=(20, 8))
figure2, xx = plt.subplots(figsize=(10,25))

line1, = ax.plot(x,y)
line2, = ax2.plot(x,y)
figure.canvas.draw()
plt.pause(0.1)

while True:
    line1.set_ydata(sin(x-time.time()))
    line2.set_ydata(sin(x+time.time()))
    figure.canvas.flush_events()


