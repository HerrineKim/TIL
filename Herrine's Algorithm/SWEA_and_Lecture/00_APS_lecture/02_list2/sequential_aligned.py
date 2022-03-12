def sequentialSearch2(a, n, key):
    i = -1
    while i < n and a[i] < key:
        i += 1
        if i < n and a[i] == key:
            return i
    return -1


print(sequentialSearch2([3, 6, 2, 43, 32, 324], 6, 43))
