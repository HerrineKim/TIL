for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = 0
    while 1:
        arr[i] -= j + 1
        if arr[i] <= 0:
            arr[i] = 0
            break
        i = (i + 1) % 8
        j = (j + 1) % 5

    print(f'#{tc}', end=' ')
    for k in range(8):
        print(arr[(i + 1 + k) % 8], end=' ')
    print()
