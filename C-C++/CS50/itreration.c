#include <cs50.h>
#include <stdio.h>
void draw(const int count);
int main(void)
{
    // testclear
    int height = get_int("Height: ");
    draw(height);
    return 0;
}

void draw(const int count)
{
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < i+1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}