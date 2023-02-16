import numpy as np


def t2r(temp):
    A = -14.6337
    B = 4791.842
    C = -115334
    D = -3.730535E+06
    rref = 10000
    r = rref*np.exp(A + B/temp + C/temp**2 + D/temp**3)
    return r

def r2t(r):
    A1 = 3.354016E-03
    B1 = 2.569850E-04
    C1 = 2.620131E-06
    D1 = 6.383091E-08
    rref = 10000
    tinv = (A1 + B1*np.log(r/rref) + C1*(np.log(r/rref))**2 + D1*(np.log(r/rref))**3)
    t = tinv**-1
    return t
    
























