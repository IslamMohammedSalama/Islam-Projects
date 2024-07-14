#include <stdio.h>
#include <cs50.h>

void meow(int count, string type);
int main(void)
{
    int max_count = get_int("How many meows? ");
    meow(max_count,"for");
    meow(max_count,"while");
    return 0;
}

void meow(int count,string type){
    if (type == "for")
    {
    printf("For Loop\n");
        for (int i = 0; i < count; i++)
        {
            printf("Meow\n");
        }
    }
    else if (type == "while")
    {
    printf("While Loop\n");
        while (count > 0)
        {
            printf("Meow\n");
            count = count - 1;
        }
    }
}