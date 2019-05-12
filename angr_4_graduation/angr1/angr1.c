#include <stdio.h>
#include <stdlib.h>

int check(char *pass)
{
    // printf("%s\n",pass);
    int len = 0;
    const char *flag = "AoiUc6Yfm=]d";
    char chr;
    len = strlen(flag);
    // printf("%d\n",len)
    if (len>20)
    {
        printf("too long!\n");
        return 0;
    }
    else
    {
        for(int i=0;i<len;i++)
        {
            // printf("%c %c\n",flag[i],pass[i]);
            
            // printf("%c ",chr);
            if(pass[i]+i!=flag[i])return 0;
        }
    }
    return 1;
}

int main(int argc, char const *argv[])
{

    char pass[64];
    printf("Enter the password:");
    if (!fgets(&pass, 63, stdin))
        return 0;
    // printf("%s\n",pass);
    if (check(&pass))
    {
        puts("Correct password!");
    }
    else
    {
        puts("Incorrect password!");
    }
    return 0;
}
