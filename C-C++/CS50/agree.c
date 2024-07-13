#include <stdio.h>
#include <cs50.h>

int main(void) {
    char a = get_char("Are You Agree: ");

    if (a == 'y' || a == 'Y')
    {
        printf("You Are Agreed ! \n");
    }
    else if (a == 'n' || a == 'N')
    {
        printf("You Are Not Agreed ! \n");
    }
}