#include <stdio.h>
#include <cs50.h>
#include <string.h>
int getstrlen(string str);
int main(void)
{
    printf("String Lenth Is: %i\n",getstrlen(get_string("Enter A String: ")));
    printf("String Lenth Is: %i\n",strlen(get_string("Enter A String: ")));
    return 0;
}
/* 
int getstrlen(string str){
    int count = 0;
    while (str[count] != '\0') count++;
    
    return count;
} */