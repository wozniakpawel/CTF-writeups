# pwnables.kr coin writeup

upon connecting to the server with `nc pwnable.kr 9007`, we are greeted with a message explaining rules:

```
        ---------------------------------------------------
        -              Shall we play a game?              -
        ---------------------------------------------------

        You have given some gold coins in your hand
        however, there is one counterfeit coin among them
        counterfeit coin looks exactly same as real coin
        however, its weight is different from real one
        real coin weighs 10, counterfeit coin weighes 9
        help me to find the counterfeit coin with a scale
        if you find 100 counterfeit coins, you will get reward :)
        FYI, you have 60 seconds.

        - How to play -
        1. you get a number of coins (N) and number of chances (C)
        2. then you specify a set of index numbers of coins to be weighed
        3. you get the weight information
        4. 2~3 repeats C time, then you give the answer

        - Example -
        [Server] N=4 C=2        # find counterfeit among 4 coins with 2 trial
        [Client] 0 1            # weigh first and second coin
        [Server] 20                     # scale result : 20
        [Client] 3                      # weigh fourth coin
        [Server] 10                     # scale result : 10
        [Client] 2                      # counterfeit coin is third!
        [Server] Correct!

        - Ready? starting in 3 sec... -
```

looks like a binary search would be of good use here. the idea is that we send a list of half the coins. if their weight is divisible by 10 (Ends with a 0), it means the fake coin is in another half. we then send the list of half of the coins we know contain the fake one. repeat the process until you find the culprit. if you automate it with python and run it locally on the server it will solve the problem pretty quickly.

it also needed some line stripping to to understand the outputs. check the coin.py for a solution. it needs to be placed somewhere in /tmp on pwnable.kr and then run locally.