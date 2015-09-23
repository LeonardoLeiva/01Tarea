import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as v
from scipy.integrate import s
import time

datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/s cm2 um')


I=0
t1_0=time.time()
for i in range(0,len(x)-1):
    dx = x_f[i+1]-x_f[i]
    dy = y_f[i+1]+y_f[i]
    I = I+dx*dy/2
t1_f=time.time()-t1_0

T=5778*u.K
K = (2*np.pi*v.h/v.c**2)*(v.k_B*T/v.h)**4

y_1=np.linspace(0.000001,np.pi/2,1000)
f_1=(np.tan(y_1)**5+np.tan(y_1)**3)/(np.exp(np.tan(y_1))-1)

I_1=0
I_2=0
I_3=0

t2_0=time.time()
for i in range(0,len(y_1)-1):
    dx = y_1[i+1]-y_1[i]
    dy = f_1[i+1]+f_1[i]
    I_1 = I_1+dx*dy/2
t2_f=time.time()-t2_0

I0=I_1+I_2+I_3
I_f=K*I0
t3_0=time.time()
i=np.trapz(y_f,x_f)
t3_f=time.time()-t3_0
t4_0=time.time()
i_f=np.trapz(f_1,y_1)
t4_f=time.time()-t4_0

print 'Integral 'I
print i
print I_f
print i_f
print t1_f
print t3_f
print t2_f
print t4_f
