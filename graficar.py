import numpy as np
import matplotlib.pyplot as plt

plt.figure( figsize=(16,5) )
data1 = np.loadtxt('data1.dat')
data2 = np.loadtxt('data2.dat')

plt.subplot(1,2,1)
plt.title('Método de Euler')
plt.plot(data1[:,0],data1[:,1],label='velocidad')
plt.plot(data1[:,0],data1[:,2],label='posición')
plt.xlabel('t')
plt.legend()
plt.subplot(1,2,2)
plt.title('Método Runge-Kutta')
plt.plot(data2[:,0],data2[:,1],label='velocidad')
plt.plot(data2[:,0],data2[:,2],label='posición')
plt.xlabel('t')
plt.legend()
plt.savefig('grafica.png')

plt.figure()
plt.plot(data1[:,1],data1[:,2], label='Euler')
plt.plot(data2[:,1],data2[:,2], label='RK4')
plt.legend()
plt.xlabel('v')
plt.ylabel('x')
plt.savefig('fase.png')
