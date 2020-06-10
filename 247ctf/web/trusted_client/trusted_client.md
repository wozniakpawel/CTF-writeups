# Trusted client

1. Check the source code of the website - there is one very long line of really obfuscated JavaScript code (called jsfuck)
2. Go to http://www.jsfuck.com/ and open developer tools (console).
3. Copy-paste the code and press "run this"
4. You will get a similar error in the console:
    VM85:3 Uncaught TypeError: Cannot read property 'value' of undefined
5. Click on the VM85:3 part and you'll get to the js code:
(function anonymous(
) {
if (this.username.value == 'the_flag_is' && this.password.value == '247CTF{FLAG_WAS_HERE}'){ alert('Valid username and password!'); } else { alert('Invalid username and password!'); }
})