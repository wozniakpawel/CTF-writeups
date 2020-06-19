# pwnable.kr collision writeup

Source code can be found in col.c.

Collision program takes 20 byte password as an argument.

check_password() function then loops over those 20 bytes interpreting them as 5 integers (each of size 4 byte). They are all added together and the result needs to match hashcode so that the following condition is met:
`if(hashcode == check_password( argv[1] )){`

The solution is to divide the hashcode into 5 smaller whole numbers, and add the remainder to one of them. col.py will calculate the values and print out the entire command that needs to be copied to the ssh client in order to get the flag.