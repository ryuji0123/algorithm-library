def convertNegativeBase(N, neg_base):
    if N == 0:
        return '0'

    ret = []
    while N != 0:
        div = int(N / neg_base)
        remainder = N - neg_base * div
        if remainder < 0:
            div += 1
            remainder -= neg_base
        N = div
        ret.append(str(remainder))
    return ''.join(reversed(ret))
