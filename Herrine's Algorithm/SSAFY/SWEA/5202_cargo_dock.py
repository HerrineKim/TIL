# 5202. 화물도크
# 복습필
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])

    cnt = 1
    j = 0
    for i in range(1, N):
        if arr[i][0] >= arr[j][1]:
            cnt += 1
            j = i

    print(f'#{tc} {cnt}')
