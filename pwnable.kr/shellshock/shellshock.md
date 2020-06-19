# pwnable.kr shellshock writeup

shellshock.c code is pretty short (credit: pwnable.kr):

```c
#include <stdio.h>
int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());
        system("/home/shellshock/bash -c 'echo shock_me'");
        return 0;
}
```

using man we find out what setresuid and setresgid do. that part will give us root permissions

however, the code still doesn't do anything 'useful' like reading the flag file. how do we force it to do that? it just echos shock_me at the moment

if you are stuck here, you probably want to have a look at google and search for shellshock. it's not cheating, you still need to figure out how to apply it!

you can notice that the system call is executing a local bash located in the user directory. that is the vulnerable bash executable

the idea is to export a function definition into an environment variable called *echo* (so that the shellshock program calls it when trying to execute "echo shock_me"). this function will cat the flag file to unveil the secret.
`export echo='() { cat ./flag; }'`

notice that `cat ./flag` will now be executed with root privileges
all that's left to do is to simply execute the program `./shellshock`