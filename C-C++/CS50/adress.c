#include <stdio.h>
// #include <cs50.h>

int main(void){

    /*int n = 100;
    int* p = &n;
    printf("%i\n", *p);
    printf("%p\n", &n);
    // printf("%p\n", p);
    return 0; */
    // string s = "HI!";
    char* s = "HI!";
    printf("%s\n", s);
    // printf("%p\n", &s[0]);
    // printf("%p\n", &s[1]);
    // printf("%p\n", &s[2]);
    // printf("%p\n", &s[3]);
    printf("%c", *s);
    printf("%c", *(s+1));
    printf("%c\n", *(s+2));
    return 0;

}