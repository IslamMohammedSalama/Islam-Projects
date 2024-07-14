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
    if (count == 0)
    {
        return;
    }
    draw(count - 1);
    
    for (int j = 0; j < count ; j++)
    {
        printf("#");
    }
    printf("\n");
    
}