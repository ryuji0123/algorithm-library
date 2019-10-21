import math

def prime_factorize(n):
    ret = []
    while n % 2 == 0:
        ret.append(2)
        n //= 2
    div = 3
    while div <= math.sqrt(n):
        if n % div == 0:
            ret.append(div)
            n //= div
        else:
            div += 2
    if n != 1:
        ret.append(n)
    return ret
