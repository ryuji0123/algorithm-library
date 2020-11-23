def binaryToGray(n):
    return n ^ (n >> 1)

def swapOddAndEven(nums):
    return [((n + 1) ^ 1) - 1 for n in nums]
