# pwn_4_graduation
# overview
## level_1 basic stack overflows
1. considering design series of stack-overflows challenges like **ret2text**,**ret2shellcode**,**ret2syscall**
2. higher-level difficulty challenges like **ret2libc**
3. maybe set some vulnerabilities like **int overflow**,**canary leakage** before ret2XXX

## level_2 basic format string bug challenges
`TODO`
## level_3 basic heap overflows
`TODO`

# challenges
## pwn_1
just a basic stack-overflow challenge with no any secure mechanism open.

## pwn_2
from *NPUCTF2018*
int overflow+ROP
> may become pwn3

## pwn_3
> may become pwn2
canary leak

## memo
gcc -fno-stack-protector -z execstack -mpreferred-stack-boundary=4 -o pwn1 pwn1.c 
Ubuntu下面的GCC默认开启了Stack Smashing Protector，
如果想在这个系统中学习缓冲区溢出的原理，在编译时要加上fno-stack-protector选项，否则运行时会出现`*** stack smashing detected ***: xxx terminated`，
而不是期望的Segmentation fault。
同时还需要加上允许栈执行的选项。 
-fno-stack-protector用来关闭gcc编译器gs验证码机制 
-z execstack用来关闭ld链接器堆栈段不可执行机制