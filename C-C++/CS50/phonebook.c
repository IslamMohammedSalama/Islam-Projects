#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
} person;
int main()
{
    /*     string strings[] = { "Ghareeb", "Osama", "Abouzeid", "Islam"};
        string phonenumbers [] = {"+20103456789", "+20113456789", "+20123456789", "+20133456789"};
        string strin = get_string("Name: ");

        for (int i = 0; i < 4; i++)
        {
            if (strcmp(strings[i],strin) == 0)
            {
                printf("Number: %s\n",phonenumbers[i]);
                return 0;
            }
        }

        printf("Not Found\n");
        return 1; */
    person peoples[] = {
        {"Ghareeb", "+20103456789"},
        {"Osama", "+20113456789"},
        {"Abouzeid", "+20123456789"},
        {"Islam", "+20133456789"}};

    // person peoples[4];
    // person peoples[4];

    // peoples[0].name = "Ghareeb";
    // peoples[0].number = "+20103456789";

    // peoples[1].name = "Osama";
    // peoples[1].number = "+20113456789";

    // peoples[2].name = "Abouzeid";
    // peoples[2].number = "+20123456789";

    // peoples[3].name = "Islam";
    // peoples[3].number = "+20133456789";
    // peoples[0].name = "Ghareeb";
    // peoples[0].number = "+20103456789";

    // peoples[1].name = "Osama";
    // peoples[1].number = "+20113456789";

    // peoples[2].name = "Abouzeid";
    // peoples[2].number = "+20123456789";

    // peoples[3].name = "Islam";
    // peoples[3].number = "+20133456789";

    string strin = get_string("Name: ");

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(peoples[i].name, strin) == 0)
        {
            printf("Found Number: %s\n", peoples[i].number);
            return 0;
        }
    }

    printf("Not Found\n");
    return 1;
}