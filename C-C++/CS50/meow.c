#include <stdio.h>
#include <cs50.h>

int main(void){
    printf("While Loop\n");
    int count = 0;
    while ( count < 10)
    {
        printf("Meow\n");
        count = count + 1;
    }
    printf("For Loop\n");
    for (int i = 0; i < 10; i++)
    {
        printf("Meow\n");
    }
    
    return 0;
}