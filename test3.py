import socket
import time
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output


secs = time.time()
print(secs)


#plt.axis([-1, 11, -0.2, 1.2])
X = np.linspace(0,9,10)
Y = np.zeros(10)
#exec(open("main.py").read())
ip = "192.168.1.189"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ip, 10000)
sock.connect(server_address)

plt.ion()
ax = plt.gca()
ax.set_autoscale_on(True)
line, = ax.plot(X,Y)

ii = 0
while True:
    ii = ii + 1
    i = ii%10
    y = np.random.random()
    y = time.time()
    sock.sendall(b"12345")
    time.sleep(0.5)
    t = sock.recv(1024)
    Y[i] = float(t)
 
    print(Y)
    
    line.set_ydata(Y)
    ax.relim()
    ax.autoscale_view(True,True,True)
    ax.axis([-1,11,min(Y)-2,max(Y)+2])
    plt.draw()
    plt.pause(0.1)

    
#     plt.axes([-0.1,1.1,65,85])



