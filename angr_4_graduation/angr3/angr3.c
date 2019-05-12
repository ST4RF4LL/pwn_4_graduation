#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
static char *check = "267?9CACHBDINPQPQVV^YZ\\_";

//243919558003665214281001
int verify() __attribute((__annotate__(("bcf"))));
int verify(char *input)
{
    unsigned char temp;
    char key[24];
    int flag=1;
    // printf("%s",input);
    for(int i=0;i<strlen(input);i++)
    {
        temp = input[i];
        temp += i*2;
        key[i]=temp;
        // input[i]+=i;
        // printf("%c",temp);
    }

    for(int i=0;i<strlen(check);i++)
    {
        if (key[i]!=check[i])
        {
            puts("Wrong!");
            return 0;
        }
    }
    puts("Correct!");
    return 1;
    
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        verify(argv[1]);
    }
    else
    {
        puts("error!");
    }
    
    return 0;
}
