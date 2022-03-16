def selection_sort(a, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
    return a


print(selection_sort([23, 5, 12, 54, 3, 4, 77], 7))