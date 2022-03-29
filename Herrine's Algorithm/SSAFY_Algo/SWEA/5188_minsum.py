# 5188. 최소합
def dfs(x, y, ssum):
    dx = [1, 0]
    dy = [0, 1]
    global res
    ssum += arr[x][y]
    if x == N-1 and y == N-1:  # 종료 조건
        if ssum < res:
            res = ssum
        return
    elif ssum > res:
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= N-1 and ny <= N-1:
            dfs(nx, ny, ssum)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    res = 10 * N * N  # 최대값
    dfs(0, 0, 0)
    print(f'#{tc} {res}')
