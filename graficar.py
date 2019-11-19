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
plt.savefig('punto5.png')

plt.figure()
plt.subplot(1,2,1)
plt.plot(data1[:,1],data1[:,2], label='Euler')
plt.legend()
plt.xlabel('v')
plt.ylabel('x')
plt.subplot(1,2,2)
plt.plot(data2[:,1],data2[:,2], label='RK4')
plt.legend()
plt.xlabel('v')
plt.ylabel('x')
plt.savefig('punto6.png')

data81 = np.loadtxt('data81.dat')
data82 = np.loadtxt('data82.dat')
data83 = np.loadtxt('data83.dat')
data84 = np.loadtxt('data84.dat')

plt.figure()
gam = [0.1, 0.5, 0.7, 0.9]
datos = [data81, data82, data83, data84]
for i in range(4):
	plt.subplot(2,2,i+1)
	plt.plot(datos[i][:,1],datos[i][:,2], label='$\gamma$ ='+str(gam[i]))
	plt.legend()
plt.savefig('punto8_fase.png')
plt.figure()
for i in range(4):
	plt.subplot(2,2,i+1)
	plt.plot(datos[i][:,0],datos[i][:,1], label='Velocidad, $\gamma$ ='+str(gam[i]))
	plt.plot(datos[i][:,0],datos[i][:,2], label='Posicion, $\gamma$ ='+str(gam[i]))
	plt.legend()
plt.savefig('punto8_XvsV.png')
