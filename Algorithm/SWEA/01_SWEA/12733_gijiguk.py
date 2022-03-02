# 12733. 기지국
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    giji = ['A', 'B', 'C']
    gijiX = []
    gijiY = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] in giji:
                gijiX.append(i)
                gijiY.append(j)

    for x in gijiX:
        for y in gijiY:
            for k in range(4):
                if arr[x][y] == 'A':
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'
                elif arr[x][y] == 'B':
                    for t in range(1, 3):
                        nx = x + dx[k]*t
                        ny = y + dy[k]*t
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'
                elif arr[x][y] == 'C':
                    for h in range(1, 4):
                        nx = x + dx[k]*h
                        ny = y + dy[k]*h
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

    for a in range(N):
        for b in range(N):
            if arr[a][b] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')
