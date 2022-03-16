def select(arr, k):
    for i in range(k):
        minidx = i
        for j in range(i+1, len(arr)):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr[k-1]


print(select([3, 5, 234, 32, 432, 66, 21, 63], 4))
