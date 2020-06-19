# pwnable.kr mistake writeup

this code in general looks like it opens a file with password, reads the contents into a buffer, then reads user input, xors every character of your input with 1 (flips the LSB) and compares that to the password. if they match, flag is printed out.

that's mostly correct, except password is not read from the password file. how?

this line will do something curious:
`if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){`

first, it will open the pasword file with read only permissions.
open() returns a file descriptor which is a number greater than zero.
then, the value of open() < 0 is evaluated
since return value of open() is greater than zero, open() < 0 will return false (0)
at the end, the evaluated zero is assigned to fd
the whole thing just boils down to fd = 0
file descriptor 0 means stdin, which also means that whatever you put in will be the password!

to solve this you need to:
- input a 10 character password
- then, input another 10 character password which is the first one with the LSB of each character flipped

for example, I chose my first password to be just ten 'b's:
`bbbbbbbbbb`

to find the other password I used python to flip the bits:
`print(10 * chr(ord('b') ^ 1))`
which results in
`cccccccccc`

Finally, run the program and enter the right values:
```
mistake@pwnable:~$ ./mistake
do not bruteforce...
bbbbbbbbbb
input password : cccccccccc
Password OK
```