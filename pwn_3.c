#include <stdio.h>
#include <unistd.h>
// canary open

int vulnerable_func()
{

    char s[40];

    while(1)
    {
        read(0,&s,40);
        puts(s);
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    setvbuf(stdin,0,2,0);
    setvbuf(stdout,0,2,0);
    vulnerable_func();
    return 0;
}