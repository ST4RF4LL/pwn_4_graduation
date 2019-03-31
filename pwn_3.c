#include <stdio.h>
#include <unistd.h>
// canary open
int getshell()
{
    system("/bin/sh");
    return 0;
}

int vulnerable_func()
{

    char s[40];

    read(0,&s,41);
    puts(s);
    read(0,&s,0x40);
    return 0;
}

int main(int argc, char const *argv[])
{
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    vulnerable_func();
    return 0;
}