import time
import logging as log


def fib_iter(n: int) -> int:
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def fib_rec(n: int) -> int:
    return n if n <= 1 else fib_rec(n - 1) + fib_rec(n - 2)


_cache = {0: 0, 1: 1}


def fib_cached(n: int) -> int:
    if n not in _cache:
        _cache[n] = fib_cached(n - 1) + fib_cached(n - 2)
    return _cache[n]


def measure(fn, n):
    t0 = time.time()
    res = fn(n)
    return res, time.time() - t0


if __name__ == '__main__':
    log.basicConfig(level=log.INFO, format='%(message)s')

    n = 30

    r1, t1 = measure(fib_iter, n)
    log.info(f'iter fib({n}) = {r1}, t = {t1:.6f}s')

    r2, t2 = measure(fib_rec, n)
    log.info(f'rec slow fib({n}) = {r2}, t = {t2:.6f}s')

    r3, t3 = measure(fib_cached, n)
    log.info(f'rec fast fib({n}) = {r3}, t = {t3:.6f}s')
