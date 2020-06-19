# pwnable.kr cmd1 writeup

looking at the source code for cmd1, it's got a filter function that will filter the argument passed to the executable.

the program will exit if any of the below are passed as part of the command:
- flag
- sh
- tmp

otherwise, it will execute the given command with root privileges

the program also modifies the environment variable PATH and overwrites it with `/thankyouverymuch`

the solution is to print contents of all the files using `cat`.
thankfully, the flag prints on the last line so it's right there when you type:
`./cmd1 "/bin/cat *"`