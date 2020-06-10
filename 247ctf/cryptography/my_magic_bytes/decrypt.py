from itertools import cycle

# convert the standard JPG file signature into a list of integers
jpg_signature = 'FF D8 FF E0 00 10 4A 46 49 46 00 01'
file_signature = [int(byte, 16) for byte in jpg_signature.split()]

# read the encrypted file, store it in memory
with open('my_magic_bytes.jpg.enc', 'rb') as inputfile:
    encrypted = inputfile.read()

# xor the encrypted file signature with the known one and figure out the key
key = cycle([encrypted[i] ^ file_signature[i] for i in range(len(file_signature))])

# decrypt the whole file using the key and save the result in a new file
with open('my_magic_bytes.jpg', 'w+b') as outputfile:
    for byte in encrypted:
        outputfile.write(bytes([byte ^ key.__next__()]))