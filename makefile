grafica.png : graficar.py data1.dat data2.dat Euler.x
	python graficar.py

data1.dat : Euler.x
	./Euler.x 10 > data1.dat
Euler.x : Euler.cpp
	c++ Euler.cpp -o Euler.x
    
data2.dat : RK.x
	./RK.x 10 > data2.dat
RK.x : RK.cpp
	c++ RK.cpp -o RK.x
	
clean :
	rm -r *.x *.dat *.png