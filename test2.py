import socket
import matplotlib.pyplot as plt
import numpy as np


plt.axis([-1, 11, -0.2, 1.2])
X = np.linspace(0,9,10)
Y = np.zeros(10)


ii = 0
while True:
    ii = ii + 1
    i = ii%10
    y = np.random.random()
    Y[i] = y
    plt.cla()
    plt.scatter(X+1,Y)
    plt.axis([-1, 11, -0.2, 1.2])
    plt.pause(0.15)

plt.show()
