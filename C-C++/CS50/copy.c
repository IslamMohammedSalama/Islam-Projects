#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void){

    char *i = get_string("i: ");
    if (i == NULL) {
        return 1;
    }
    char *j = malloc(strlen(i) + 1);
    if (j == NULL){
        return 1;
    }
    strcpy(j, i);
    if (strlen(i) > 0) {
    j[0] = toupper(j[0]);
     }
    printf("%s\n", i);
    printf("%s\n", j);
    free(j);
    return 0;
    // return 0;

}
