#include <stdio.h>
int getshell()
{
    system("/bin/sh");
    return 0;
}

int vulnerable_func()
{
    int i= 5;
    char s[0x40];
    while(i--)
    {
        gets(s);
        puts(s);
        return 0;    
    }
    
}

int main(int argc, char const *argv[])
{
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    vulnerable_func();
    return 0;
}
