import sys
import signal
import time
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, handler)  
signal.alarm(5)

try:
    with open(sys.argv[1]) as f:
        n = int(f.read())
        p = 2
        while p * p <= n:
            if n % p == 0 and is_prime(p):
                q = n // p
                if is_prime(q):
                    print(f"{n}={p}*{q}")
                    break
            p += 1
except TimeoutError:
    print("Time limit exceeded")