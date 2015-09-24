import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as v


#define constantes
T=5778*u.K
K = (2*np.pi*v.h/v.c**2)*(v.k_B*T/v.h)**4

#define arreglo que se usara
y_1=np.linspace(0,np.pi/2,1000)
f_1=(np.tan(y_1)**5+np.tan(y_1)**3)/(np.exp(np.tan(y_1))-1)

'''
esto es parte de un intento de mejorar el metodo que quedara en espera
y_2=np.linspace(np.pi/6,np.pi/3,1000)
f_2=(np.tan(y_2)**5+np.tan(y_2)**3)/(np.exp(np.tan(y_2))-1)

y_3=np.linspace(0,np.pi/2,1000)
f_3=(np.tan(y_3)**5+np.tan(y_3)**3)/(np.exp(np.tan(y_3))-1)

'''
#parte del intento de mejorar el metodo
I_1=0
I_2=0
I_3=0

#integral por trapecios
for i in range(1,len(y_1)-1):
    dx = y_1[i+1]-y_1[i]
    dy = f_1[i+1]+f_1[i]
    I_1 = I_1+dx*dy/2



#nuevo arreglo para calcular por simpson
y_2=np.linspace(0,np.pi/2,500)
f_2=(np.tan(y_1)**5+np.tan(y_1)**3)/(np.exp(np.tan(y_1))-1)
y_3=np.linspace(0,np.pi/2,1000)
f_3=(np.tan(y_1)**5+np.tan(y_1)**3)/(np.exp(np.tan(y_1))-1)

Is_2=0
Is_3=0
#calculo por simspon
for i in range(1,len(y_2)-1):
    dx = y_2[i+1]-y_2[i]
    dy = f_2[i+1]+f_2[i]
    Is_2 = Is_2+dx*dy/2

for i in range(1,len(y_3)-1):
    dx = y_3[i+1]-y_3[i]
    dy = f_3[i+1]+f_3[i]
    Is_3 = Is_3+dx*dy/2

#valores de las integrales
Is=(4/3)*Is_3-(1/3)*Is_2
I=I_1+I_2+I_3
#multiplicando por las constantes
I_f=K*I
I2_f=K*Is

print "Valor de la Integral (Metodo de trapecios)",I
print "Valor de la Integral (Metodo de Simpson)",Is
print "Valor de la integral pedida trapecios (P)=",I_f
print "Valor de la integral pedida simpson (P)=",I2_f
