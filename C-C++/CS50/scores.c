#include <stdio.h>
#include <cs50.h>

float average(int lenth, int arrey[]);
const int REPETITIONS = 3;

int main(void){
/*     int score1 = 72;
    int score2 = 73;
    int score3 = 33; */
    int scores[REPETITIONS];
    for (int i = 0; i < REPETITIONS; i++)
    {
        scores[i] = get_int("Score %i: ",i);
    }
    printf("Average: %f\n",average(REPETITIONS, scores));
    return 0;

}


float average(int lenth , int arrey[]){
    int sum = 0;
    for (int i = 0; i < lenth; i++)
    {
        sum = sum + arrey[i];
    }
    return (float) sum / lenth;
}