#include <cs50.h>
#include <stdio.h>
float add(float x, float y);
float removee(float x, float y);
float mati(float x, float y);
float dev(float x, float y);
float main(void){
    float x = get_float ("x: ");
    float y = get_float ("y: ");
    printf("%.1f\n", add(
                    (float)x,(float)y
                       ));
    printf("%.2f\n", removee(
                    (float)x,(float)y
                       ));
    printf("%.3f\n", mati(
                    (float)x,(float)y
                       ));
    printf("%.4f\n", dev(
                    (float)x,(float)y
                       ));
}


float add(float x,float y){
    return x+y;
}

float removee(float x,float y){
    return x-y;
}

float mati(float x,float y){
    return x*y;
}

float dev(float x,float y){
    return x/y;
}