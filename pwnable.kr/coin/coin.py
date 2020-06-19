import socket

hostname = '0'
port = 9007
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def submit(lo, hi):
    stdin = ''
    for i in range(lo, hi + 1):
        stdin += '{} '.format(str(i))
    sock.send('{}\n'.format(stdin).encode())
    res = sock.recv(64).rstrip().decode()
    if (res[-1] == '9'):
        return True
    return False

def guess():
    n, c = get_nc()
    lo, hi = 0, n
    for i in range(c+1):
        if i == c:
            sock.send('{}\n'.format(lo).encode())
            sock.recv(64)
            break
        oldhi = hi
        hi = int(lo + (hi - lo) / 2)
        if not submit(lo, hi):
            lo = hi + 1
            hi = oldhi

def get_nc():
    data = ""
    while(not data):
        data = sock.recv(128).rstrip().decode()
        n, c = data.split(' ')
        n = int(n.replace('N=', ''))
        c = int(c.replace('C=', ''))
        return n, c

def main():
    sock.connect((hostname, port))
    sock.recv(2048)
    for i in range(100):
        guess()
    print(sock.recv(512).decode())
    sock.close()

if __name__ == '__main__':
    main()