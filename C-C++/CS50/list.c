#include <stdio.h>
#include <stdlib.h>

int main(){
    int *list = malloc(3 * sizeof(int));

    if (list == NULL)
    {
        return 1 ; 
    }
    
    
    list[0] = 1 ;
    list[1] = 2 ;
    list[2] = 3 ;
    
    int *tmp = malloc(3 * sizeof(int));

    if (tmp == NULL)
    {
        free(list);
        return 1 ; 
    }

    for (int i = 0; i < 4; i++)
    {
        tmp[i] = list[i];
    }
    
    tmp[3] = 4 ;
    list = tmp ;
    
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n",tmp[i]);
    }
    
    return 0 ; 

}