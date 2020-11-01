def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def prime_factorize_set(n):
    ret = set()
    while n % 2 == 0:
        ret.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            ret.add(i)
            n //= i
        else:
            i += 2
    if n != 1:
        ret.add(n)
    return ret
