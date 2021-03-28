def flatten(arr):
    ret = []
    i = 0
    while i < len(arr):
        if isinstance(arr[i], int):
            yield arr[i]
        else:
            for elem in flatten(arr[i]):
                yield elem
        i += 1
