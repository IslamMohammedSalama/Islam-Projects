#include <cs50.h>
#include <stdio.h>
void row_and_cols(int rows, int cols);
int main(void){
    // testclear
    
    int rows;
    do
    {
        rows = get_int("Rows: ");
    } while (rows < 1);
    
    int cols;
    do
    {
        cols = get_int("Cols: ");
    } while (cols < 1);
    row_and_cols(
        rows,
        rows);
    return 0;
}

void row_and_cols(const int rows, const int cols){
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}