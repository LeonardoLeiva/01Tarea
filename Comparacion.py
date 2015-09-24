import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as v

#proceso repetido de etapas anteriores
datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/s cm2 um')


I=0
for i in range(0,len(x)-1):
    dx = x_f[i+1]-x_f[i]
    dy = y_f[i+1]+y_f[i]
    I = I+dx*dy/2
Is=I.to('J/m2 s')

T=5778*u.K
K = (2*np.pi*v.h/v.c**2)*(v.k_B*T/v.h)**4

y_1=np.linspace(0,np.pi/2,1000)
f_1=(np.tan(y_1)**5+np.tan(y_1)**3)/(np.exp(np.tan(y_1))-1)

I_1=0
I_2=0
I_3=0


for i in range(1,len(y_1)-1):
    dx = y_1[i+1]-y_1[i]
    dy = f_1[i+1]+f_1[i]
    I_1 = I_1+dx*dy/2


I0=I_1+I_2+I_3
I_f=K*I0

#calculo de radio mediante la formula de la constante solar
R=((Is/I_f)**0.5)*v.au

print "Radio de la Tierra estimado=",R
