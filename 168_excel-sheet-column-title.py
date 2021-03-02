class Solution:
    def convertToTitle(self, n: int) -> str:
        def num2alpha(N):
            ret = ''
            while 0 < N:
                N -= 1
                ret += chr(ord('A') + N % 26)
                N //= 26
            return ret[::-1]
        
        return num2alpha(n)
