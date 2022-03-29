def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    queue = []  # 큐 생성
    queue.append((i, j))  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문표시
    while queue:  # 큐가 비어있지 않을 동안 반복
        i, j = queue.pop(0)
        if maze[i][j] == 3:  # visit(t) t에서 할 일 처리
            return visited[i][j] - 2  # 출발 도착 칸 제외
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # i, j에 인접한 칸에 대해
            ni, nj = i + dj, j + dj  # 주변 칸 좌표
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))  # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착지를 찾지 못한 경우


def dfs(i, j, N, c):  # c 지나온 칸 수
    global minV
    if maze[i][j] == 3:
        if minV > c:
            minV = c
    else:
        maze[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                dfs(ni, nj, N, c+1)
        maze[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = fstart(N)
    # sti, stj = -1, -1
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j] == 2:
    #             sti, stj = i, j
    #     if sti != -1:
    #         break
    # ans = bfs(sti, stj, N)
    # 재귀 dfs
    minV = 100000
    dfs(sti, stj, N, 0)
    print(f'#{tc} {minV-1}')
