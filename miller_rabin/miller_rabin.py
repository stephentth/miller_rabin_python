import logging
import random

def miller_rabin(n: int, k: int=3):
    logging.debug(f"Got {n} with {k}")
    if not isinstance(n, int) and not isinstance(k, int):
        raise ValueError("Expect integet number")

    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    logging.debug(f"{n} - 1 = 2^{s} * {d}")

    for i in range(k):
        a = random.randrange(2, n-1)
        x = a ** d % n
        if x == 1: continue
        for j in range(s):
            if x == n-1: break
            x = x**2 % n
        else:
            logging.debug(f"Result: {n} is not prime with k={3}.")
            return False
    logging.debug(f"Result: {n} is prime with k={3}.")
    return True
