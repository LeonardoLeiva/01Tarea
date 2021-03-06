import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as v
from scipy import integrate as s
import time
#mismo metodo anterior
datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/s cm2 um')

#se agregan contadores a cada calculo de integral
I=0
t1_0=time.time()
for i in range(0,len(x)-1):
    dx = x_f[i+1]-x_f[i]
    dy = y_f[i+1]+y_f[i]
    I = I+dx*dy/2
t1_f=time.time()-t1_0

T=5778*u.K
K = (2*np.pi*v.h/v.c**2)*(v.k_B*T/v.h)**4

#aqui se parte el arreglo un poco pasado de 0 en vez de eliminar el primer termino
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

#calculo de integrales por medio del trapecio pre-configurado
t3_0=time.time()
i=s.trapz(y_f,x_f)
t3_f=time.time()-t3_0
t4_0=time.time()
i_f=K*s.trapz(f_1,y_1)
t4_f=time.time()-t4_0

#calculo de la 2da integral por medio de quad
t5_0=time.time()
f= lambda x: (x**3)/(np.exp(x) - 1)
integ=s.quad(f,0,np.inf)
Iq=K*integ[0]
t5_f=time.time()-t5_0

#comparaciones entre las integrales
dI1=I-i
dI2=I_f-i_f
dI3=I_f-Iq
#comparaciones entre tiempos de demora
dt1=t1_f-t3_f
dt2=t2_f-t4_f
dt3=t2_f-t5_f


print "Valor de la integral (funcion quad)=", integ[0]
print "Diferencia entre integral de la parte 2 calculada por el metodo creado y el de trapecios=",dI1
print "Diferencia entre integral de la parte 3 calculada por el metodo creado y el de trapecios=",dI2
print "Diferencia entre integral de la parte 3 calculada por el metodo creado y la funcion quad=",dI3
print "Diferencia de tiempo tomado entre los metodos (integral 1)=",dt1
print "Diferencia de tiempo tomado entre los metodos trapecios (integral 2)=",dt2
print "Diferencia de tiempo tomado entre los metodos quad (integral 2)=",dt3
