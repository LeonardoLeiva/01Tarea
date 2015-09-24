import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
'''
Solo grafica los datos del archivo entregado luego de separarlos
'''

datos = np.loadtxt("sun_AM0.dat") #importa los datos

#separa los datos
x = datos[:,0]
y = datos[:,1]

#da unidades a las variables
x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

#transforma a cgs
x_f=x_u.to('um')
y_f=y_u.to('erg/(s cm2 um)')

#configuraciones del gráfico
plt.figure(1)
plt.clf()

plt.plot(x_f, y_f)
plt.xlabel('$\lambda$ [$\mu m$]')
plt.ylabel('Flujo[$erg/(s*cm^2*um)$]')
plt.title('Flujo vs Longitud de Onda')

plt.xlim(0,4)
plt.show()
#plt.savefig('Grafico.png')
