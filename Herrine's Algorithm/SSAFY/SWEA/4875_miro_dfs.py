def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


def dfs1(i, j, N):  # 스택 사용
    stack = []      # 스택생성
    visted = [[0]*N for _ in range(N)]  # visited생성
    while 1:
        # i, j 칸 방문
        visted[i][j] = 1
        if maze[i][j] == 3:  # 목적지면
            return 1
        # 현재 위치 i, j에서 갈 수 있는 곳 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 미로 내부, 벽이 아니고(통로 or 도착칸), 방문하지 않은 칸
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visted[ni][nj]==0:
                stack.append((i, j))    # 현재 위치 스택에 저장
                i, j = ni, nj           # ni, nj로 이동
                break                   # ni, nj 방문
        else: # 갈수있는 칸이 없으면
            if stack:                   # 뒷걸음질
                i, j = stack.pop()
            else:                       # 출발지까지 되돌아온경우
                break                   # 3번칸에 도착할 수 없는 상황
    return 0


def dfs2(i, j, N):      # 재귀
    visited[i][j] = 1
    if maze[i][j]==3:
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                if dfs2(ni, nj, N):
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

    # 미로 탐색
    # ans = dfs1(sti, stj, N)
    # print(f'#{tc} {ans}')
    visited = [[0]*N for _ in range(N)] # dfs2 용
    print(f'#{tc} {dfs2(sti, stj, N)}')