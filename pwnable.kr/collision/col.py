#!/usr/bin/env python3

import struct

hashcode = 0x21DD09EC

n1 = hashcode // 5
n2 = hashcode - 4 * n1

answer = repr(struct.pack('<i', n1) * 4 + struct.pack('<i', n2))[1:]
print(f'./col `echo -n -e {answer}`')