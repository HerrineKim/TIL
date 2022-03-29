for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for _ in range(N):
        maxIdx = arr.index(max(arr))
        minIdx = arr.index(min(arr))
        arr[maxIdx] -= 1
        arr[minIdx] += 1

    print(f'#{tc} {max(arr) - min(arr)}')
