import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u

datos = np.loadtxt("sun_AM0.dat")

x = datos[:,0]
y = datos[:,1]

x_u=x*u.nm
y_u=y*u.W*(u.m**-2)*(u.nm**-1)

x_f=x_u.to('um')
y_f=y_u.to('erg/(s cm2 um)')

plt.figure(1)
plt.clf()

plt.plot(x_f, y_f)
plt.xlabel('$\lambda$ [$\mu m$]')

plt.xlim(0,4)
plt.show()
