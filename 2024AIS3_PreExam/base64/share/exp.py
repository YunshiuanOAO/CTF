from pwn import *
r = process('./base64encoder')
payload = cyclic(5600)
gdb.attach(r)
r.sendlineafter('Text: ',payload)
r.interactive()