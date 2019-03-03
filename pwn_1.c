#include <stdio.h>
int getshell()
{
    system("/bin/sh");
    return 0;
}

int vulnerable_func()
{
    char s[0x40];
    puts("Just input something?");
    gets(s);
    return 0;    
    
}

int main(int argc, char const *argv[])
{
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    vulnerable_func();
    return 0;
}
