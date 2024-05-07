#include <iostream>
// #include <stdio.h>
using namespace std;
string make(int num)
{
    system("clear");
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            printf("#");
        }
        cout << endl;
    }
    return "";}
string old_or_even(int number)
{
    if (number % 2 == 0){
        return "old";
    }
    else
    {
        return "even";
    }
    
}
int main(){
    int i;
    do
    {
        cout << "enter a number : ";
        cin >> i;
        if (i <= 0 )
        {
            printf("enter a number > 0\n");
        }
        
    } while (i <= 0);
    make(i);
    return 0;
}