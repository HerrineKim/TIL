T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]
    for i in range(len(arr)):
        if arr[i]>maxV:
            maxV = arr[i]

    print(f'#{tc} {maxV}')