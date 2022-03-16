T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    maxV = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for k in range(1, arr[i][j]+1):
                    ni, nj = i + di*k, j + dj*k
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]
            if maxV < s:
                maxV = s
    print(f'#{tc} {maxV}')

