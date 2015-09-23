import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
import time

datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/(s cm2 um)')

I=0
t0=time.time()
for i in range(0,len(x)-1):
    dx = x_f[i+1]-x_f[i]
    dy = y_f[i+1]+y_f[i]
    I = I+dx*dy/2
tf=time.time()-t0

print I
print tf
