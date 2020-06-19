# pwnables.kr random writeup

so the random.c code generates a randon unsigned integer using random() function and asks user to input a key in stdin

if key xored with random equals 0xdeadbeef, the flag is given:
`(key ^ random) == 0xdeadbeef`

random() function defaults to a seed equal 1. This will generate the same number ever time it's run. To check what is the 'random' number, simply create a different program somwehere in /tmp to print out the value:

```c
#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();        // random value!
        printf("random: %d\n", random);
        return 0;
}
```

then, compile it with:
`gcc find_random.c -o find_random`

then, run it:

```
random@pwnable:/tmp/atedf$ ./find_random
random: 1804289383
```

copy the 'random' number and xor it with 0xdeadbeef (using python) to get the key value:

```python
>>> 0xdeadbeef ^ 1804289383
3039230856
```

that is the answer. run the random program and get the flag.