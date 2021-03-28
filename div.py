from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


from math import gcd


def gcdFromLeftAndRight(N, A):
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for idx in range(1, N + 1):
        L[idx] = gcd(L[idx - 1], A[idx - 1])
        R[N - idx] = gcd(R[N + 1 - idx], A[N - idx])
    return L, R


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


from math import sqrt


def factorization(n):
    arr = []
    tmp = n
    div = 2
    while div * div <= n:
        if tmp % div == 0:
            cnt = 0
            while tmp % div == 0:
                cnt += 1
                tmp //= div
            arr.append([div, cnt])
        div += 1

    if tmp != 1:
        arr.append([tmp, 1])

    if len(arr) == 0:
        arr.append([n, 1])

    return arr
