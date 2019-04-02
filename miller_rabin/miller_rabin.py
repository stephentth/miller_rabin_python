import random

def miller_rabin(n: int, k: int=3):
    if not isinstance(n, int) and not isinstance(k, int):
        raise ValueError("Expect integer number")

    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n-1)
        x = a ** d % n
        if x == 1: continue
        for _ in range(s):
            if x == n-1: break
            x = x**2 % n
        else:
            return False
    return True
