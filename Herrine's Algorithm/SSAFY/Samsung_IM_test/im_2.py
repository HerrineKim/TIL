T = int(input())
for tc in range(1, T+1):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    X = 0
    Y = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                X = x
                Y = y
    for k in range(4):
        for h in range(N):
            nx = X + (dx[k] * h)
            ny = Y + (dy[k] * h)
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                elif arr[nx][ny] == 1:
                    break

    for a in range(N):
        for b in range(N):
            if arr[a][b] == 0:
                res += 1
    print(f'#{tc} {res}')
