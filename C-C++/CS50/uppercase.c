#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
string uppercase(string before);
int main(void)
{
    string before = get_string("Before: ");
    printf("After 1: %s\n", uppercase(before));
    return 0;
}

string uppercase(string before){
    for (int i = 0, length = strlen(before); i < length; i++){
        before[i] = toupper(before[i]);
        // if (before[i] >= 'a' && before[i] <= 'z')
        // {
        //     // before[i] = before[i] - 32;
        //     before[i] = toupper(before[i]);
        // }
    }
    return before;
}