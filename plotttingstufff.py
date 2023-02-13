import matplotlib.pyplot as plt
import numpy as np
import p

x = np.linspace(0,1,100)

fig,ax = plt.subplots()

p1, = ax.plot(x,np.sin(x))
#plt.pause(0.1)

# def p():
#     while True:
#         try:
#             plt.pause(0.1)
#         except KeyboardInterrupt:
#             break

# import time
# while True:
#     try:
#         print(10/1)
#     except KeyboardInterrupt:
#         print(5)
#     finally:
#         print(6)
#         print(7)
#     time.sleep(0.2)






