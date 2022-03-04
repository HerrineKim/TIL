def ss(a, x):
    n = len(a)  # 입력 크기 n
    for i in range(n):
        if x == a[i]:
            return i
    return -1
