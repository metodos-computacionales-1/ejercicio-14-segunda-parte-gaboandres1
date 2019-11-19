punto5 : graficar.py data81.dat data82.dat data83.dat data84.dat data1.dat data2.dat Euler.x
	python graficar.py
data81.dat : RK.x
	./RK.x 1 > data81.dat
data82.dat : RK.x
	./RK.x 2 > data82.dat
data83.dat : RK.x
	./RK.x 3 > data83.dat
data84.dat : RK.x
	./RK.x 4 > data84.dat
data1.dat : Euler.x
	./Euler.x 10 > data1.dat
Euler.x : Euler.cpp
	c++ Euler.cpp -o Euler.x
    
data2.dat : RK.x
	./RK.x 0 > data2.dat
RK.x : RK.cpp
	c++ RK.cpp -o RK.x
	
clean :
	rm -r *.x *.dat *.png