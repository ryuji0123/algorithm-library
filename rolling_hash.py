def queryUsingRollingHash(s, q):
    lq = len(q)
    ls = len(s)
    rolling_hash = {
            s[i: i + lq] for i in range(ls)
            } | {
            s[i: i + lq - 1] for i in range(ls)
            }
    return q in rolling_hash
