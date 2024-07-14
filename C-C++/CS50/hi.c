#include <stdio.h>
#include <cs50.h>
int main(void){
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';
    string s = "HI!";
    printf("%c%c%c\n",c1,c2,c3);
    printf("%c%c%c\n",c1,c2,c3);
    printf("%s\n",s);
    printf("%c %c %c\n",s[0],s[1],s[2]);
    printf("%i %i %i\n",s[0],s[1],s[2]);
    return 0;
}