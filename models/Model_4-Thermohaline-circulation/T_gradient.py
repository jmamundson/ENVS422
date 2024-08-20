import numpy as np
from matplotlib import pyplot as plt
import matplotlib

font = {'family':'serif', 'weight' :'normal', 'size':9}
matplotlib.rc('font', **font)
#matplotlib.rc('text',usetex=True)
matplotlib.rc('lines',linewidth=1,color='w')

lat = np.array([0,90])
T_eq = np.array([1,0])
T = np.array([1.2,-0.2])


plt.figure(1,figsize=(6,3))

plt.plot(lat,T_eq,'k',lat,T,'k--')
plt.arrow(10, 1.03 ,0, -0.08,head_width=1.5,head_length=0.05,facecolor='k')
plt.arrow(80, -0.03 ,0, 0.08,head_width=1.5,head_length=0.05,facecolor='k')
#plt.text(15,1,'Temperature profile at time $t$')
plt.xlim([0,90])
plt.xlabel(r'Latitude [$^\circ$]')
plt.yticks([])
plt.ylabel(r'Temperature')

plt.tight_layout()

plt.savefig('T_gradient.jpg',format='jpg',dpi=300)