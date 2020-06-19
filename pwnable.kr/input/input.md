# pwnable.kr input writeup

so far, I only got as far as clearing stage 1:

```
if(argc != 100) return 0;
  if(strcmp(argv['A'],"\x00")) return 0;
  if(strcmp(argv['B'],"\x20\x0a\x0d")) return 0;
  printf("Stage 1 clear!\n");
```

the code above checks the following:
- there must be 100 bytes passed as an argument
- 65th character in the argument must be a null byte (\x00)
- that must be followed by the following bytes: \x20\x0a\x0d

I achieved that using the code below direcly in pwnables.kr shell:

```
./input `python3 -c 'print("\x41 " * 64)'` "" "$(python3 -c "print('\x20\x0a\x0d')")" `python3 -c 'print("\x41 " * 33)'`
```

this uses python3 to pass raw bytes to the program input