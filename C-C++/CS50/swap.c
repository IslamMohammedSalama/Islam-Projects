#include <stdio.h>

void swap(int *a, int *b);

int main(void){
    int x = 1;
    int y = 2;

    printf("x is %i\n", x);
    printf("y is %i\n", y);

    swap(&x, &y);

    printf("x is %i\n", x);
    printf("y is %i\n", y);
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
