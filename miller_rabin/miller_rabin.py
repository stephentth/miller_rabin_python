import random
from concurrent.futures import ProcessPoolExecutor, as_completed

def miller_rabin(n: int, k: int=3) -> bool:
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

def miller_rabin_mutilprocess(n: int, k:int= 3) -> bool:
    with ProcessPoolExecutor() as executor:
        futures = []
        for _ in range(k):
            futures.append(executor.submit(miller_rabin, n, 1))
        
        for future in as_completed(futures):
            result = future.result()
            if result is False:
                return False
    return True
