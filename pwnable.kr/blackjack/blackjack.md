# pwnable.kr blackjack writeup

at the beginning we are given a source code to analyse:
http://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html

also we know we need to be pretty rich to solve this pwnable:
```
I like to give my flags to millionares.
how much money you got?
```

there are at least 2 vulnerabilities in the code:
1. if you bet more money than you have, it will tell you to bet again. However, this time the check doesn't take place so you can bet anything
```c
int betting() //Asks user amount to bet
{
 printf("\n\nEnter Bet: $");
 scanf("%d", &bet);
 
 if (bet > cash) //If player tries to bet more money than player has
 {
        printf("\nYou cannot bet more money than you have.");
        printf("\nEnter Bet: ");
        scanf("%d", &bet);
        return bet;
 }
 else return bet;
} // End Function
 
```
2. you can also bet a negative amount - then, you want to lose. losing a negative amount = winning a postive one!
```c
if(p>21) //If player total is over 21, loss
         {
             printf("\nWoah Buddy, You Went WAY over.\n");
             loss = loss+1;
             **cash = cash - bet;**
             printf("\nYou have %d Wins and %d Losses. Awesome!\n", won, loss);
             dealer_total=0;
             askover();
         }
```

after winning or losing you need to play another game to get the flag.