#include <iostream>
#include <cmath>

float f(float);

const double K = 100;
const double M = 2;
const int LAMBDA = 1;
int main(int argc, char **argv){
    
    int T = atoi(argv[1]);
    float h = 0.01;
    float v_anterior = 0;
    float v_siguiente = v_anterior;
    
    float x_anterior = 1;
    float x_siguiente = x_anterior;
    
    float t;
    for(t=0; t<=T;t+=h){
        std::cout << t << "\t" << v_siguiente << "\t" << x_siguiente << std::endl;
        v_siguiente = v_anterior + h*f(x_anterior);
        x_siguiente = x_anterior + h*v_anterior;
        
        v_anterior = v_siguiente;
        x_anterior = x_siguiente;
        
    }
    std::cout << t << "\t" << v_siguiente << "\t" << x_siguiente << std::endl;
    
    return 0;
}

float f(float y){
    return -K/M*pow(y,LAMBDA);
}