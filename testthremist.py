import numpy as np
import matplotlib.pyplot as plt
from NTCLE100E3103JB0 import *


A = -14.6337
B = 4791.842
C = -115334
D = -3.730535E+06

A1 = 3.354016E-03
B1 = 2.569850E-04
C1 = 2.620131E-06
D1 = 6.383091E-08

B2595 = 3977

rref = 10000
tref = 273.15 + 25
temp = 273.15 + 95

r = rref*np.exp(A + B/temp + C/temp**2 + D/temp**3)

#r = 11300

tinv = (A1 + B1*np.log(r/rref) + C1*(np.log(r/rref))**2 + D1*(np.log(r/rref))**3)

t = tinv**-1

print(r)
print(t-273.15)





x = np.arange(0,125,0.1)
y = t2r(x+273.15)

vout  = 1000/(1000+y)
vout2  = y/(1000+y)

fig,ax = plt.subplots()
line, = ax.plot(x,y,'-b')

fig2,ax2 = plt.subplots()
line2, = ax2.plot(x,vout,'-b')

fig3,ax3 = plt.subplots()
line3, = ax3.plot(x,vout2,'-b')

while True:
    plt.pause(0.1)







