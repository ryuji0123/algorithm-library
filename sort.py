def radixSort(nums):
    M = max([len(str(n)) for n in nums])
    for i in range(M):
        bucket = [[] for _ in range(10)]
        for n in nums:
            key = n // pow(10, i) % 10
            bucket[key].append(n)
        nums = [v for b in bucket for v in b]
        
    return nums
