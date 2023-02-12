import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
 
plt.ion()

figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(x, y)
line2, = ax.plot(x, np.tan(x))
 


for _ in range(50):
    new_y = np.sin(x-0.5*_)
    new_y2= np.tan(x-0.5*_)
    line1.set_xdata(x)
    line1.set_ydata(new_y)
    line2.set_xdata(x)
    line2.set_ydata(new_y2)
    ax.axis([0, 10, -3, 3])
    figure.canvas.draw()
 
    figure.canvas.flush_events()
 
    time.sleep(0.1)