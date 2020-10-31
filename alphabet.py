def num2alpha(N):
    ret = ''
    while 0 < N:
        N -= 1
        ret += chr(ord('a') + N % 26)
        N //= 26
    return ret[::-1]
