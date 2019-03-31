#include <stdio.h>
#include <unistd.h>

int vulnerable_func()
{

    char s[512];
    int key=0x9876;
    printf("give me the key!%p\n",&key);
    // scanf("%s",s);
    read(0,&s,512);
    printf(s);
    if(key == 0x1234)
    {
        system("cat flag");
    }
    else
    {
        puts("wrong answer!");
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