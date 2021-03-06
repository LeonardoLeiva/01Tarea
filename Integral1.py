import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
import time

'''
Calcula integral por metodo del trapecio. Devuelve el valor de la integral sola,
multiplicado por sus constantes y el tiempo que tarda
'''

#toma datos, da unidades y las transforma
datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/(s cm2 um)')

#Calculo de integral por trapecios. Tambien cuenta el tiempo de ejecucion
I=0
t0=time.time()
for i in range(0,len(x)-1):
    dx = x_f[i+1]-x_f[i]
    dy = y_f[i+1]+y_f[i]
    I = I+dx*dy/2
tf=time.time()-t0
Id=I.to('W/m2') #cambiaunidades de medida a SI

print "Integral Calculada por Metodo de Trapecios=", I #solo la integral
print "Tiempo que toma el alrgoritmo=", tf
print "Integral Calculada por Metodo de Trapecios en SI=", Id #integral*constantes
