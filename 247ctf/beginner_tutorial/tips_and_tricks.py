from pwnlib.tubes.remote import remote

conn = remote('9e3afa8520c88bb5.247ctf.com',50379)
for i in range(2):
    print(conn.recvline())
for i in range(501):
    a = conn.recvline().decode().split()
    print(a)
    ans = int(a[-1].replace('?', '')) + int(a[-3])
    print(ans)
    conn.send(f'{ans}\r\n'.encode())
    print(conn.recvline())
print(conn.recvline())
conn.close()