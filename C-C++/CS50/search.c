#include <stdio.h>
#include <cs50.h>
#include <string.h>

/* int main(){
    int nums[] = { 20, 500, 10, 5, 100, 1, 50};

    int nuum = get_int("Number: ");

    for (int i = 0; i < 7; i++)
    {
        if (nums[i] == nuum)
        {
            printf("Found\n");
            return 0;
        }
    }

    printf("Not Found\n");
    return 1;
} */

int main(){
    string strings[] = { "Ghareeb", "Osama", "Abouzeid", "Islam"};
    string strin = get_string("String: ");
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(strings[i],strin) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }

    printf("Not Found\n");
    return 1;
    
}