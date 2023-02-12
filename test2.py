

import socket
import matplotlib.pyplot as plt
import numpy as np


plt.axis([-1, 11, -0.2, 1.2])
X = np.linspace(0,9,10)
Y = np.zeros(10)

for i in range(10):
    print(i)
    y = np.random.random()
    Y[i] = y
    plt.cla()
    plt.scatter(X[0:i+1]+1,Y[0:i+1])
    plt.axis([-1, 11, -0.2, 1.2])
    plt.pause(0.15)

plt.show()
