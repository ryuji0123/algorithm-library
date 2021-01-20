from itertools import accumulate


def maxSumTwoNoOverlap(self, A, L, M):
    N = len(A)
    pre_sum = [0] + list(accumulate(A))
    ret = 0
    for i in range(N - L + 1):
        sl = pre_sum[i + L] - pre_sum[i]
        sm = 0
        j = 0
        while j + M <= i:
            sm = max(sm, pre_sum[j + M] - pre_sum[j])
            j += 1
        j = i + L
        while j + M <= N:
            sm = max(sm, pre_sum[j + M] - pre_sum[j])
            j += 1
        ret = max(ret, sl + sm)
    return ret
