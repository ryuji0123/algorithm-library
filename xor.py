def xorFromLeftAndRight(N, A):
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for idx in range(1, N + 1):
        L[idx] = L[idx - 1] ^ A[idx - 1]
        R[N - idx] = R[N + 1 - idx] ^ A[N - idx]
    return L, R


def xorTotal(N, A):
    L = [0] * (N + 1)
    for idx in range(1, N + 1):
        L[idx] = L[idx - 1] ^ A[idx - 1]
    return L
