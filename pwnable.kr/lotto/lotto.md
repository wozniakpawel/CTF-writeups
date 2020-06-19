# pwnable.kr lotto writeup

this code reads 6 bytes of data from stdin (fd = 0), then generates 6 truly random bytes using /dev/urandom. they are in range 1-45 so our input has to match that

then, the code compares our submission to the random numbers and counts the score. this is actually where the vulnerability lies:
```
// calculate lotto score
int match = 0, j = 0;
for(i=0; i<6; i++){
        for(j=0; j<6; j++){
                if(lotto[i] == submit[j]){
                        match++;
                }
        }
}
```

for each random number it goes through every single submitted number and adds 1 to the score if they are matching. we need score of 6 to read the flag. we can just submit 6 numbers that are the same and if one of the random numbers is matching, it will count a point for each.

you might need to run the program a few times until the random number is matching your submission

for example, looking at the [ASCII table](http://www.asciitable.com/), we can see that "!" character has a decimal value of 33. That number is less than 45 so we can use `!!!!!!` as a submission. You can submit any other character that is less than 45 in ASCII.