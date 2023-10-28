import sys
import signal
import time

def handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            n = int(line.strip())
            p = 2
            while p * p <= n:
                if n % p == 0:
                    q = n // p
                    print(f"{n}={p}*{q}") 
                    break
                p += 1
            else:
                print(f"{n} is prime")
except TimeoutError:
    print("Time limit exceeded")