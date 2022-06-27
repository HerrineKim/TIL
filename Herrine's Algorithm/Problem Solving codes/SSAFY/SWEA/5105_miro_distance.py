def bfs(i, j, N):
    q = []  # 큐생성
    visited = [[0]*N for _ in range(N)] # visited생성
    q.append((i,j))     # 시작점 인큐
    visited[i][j] = 1   # 처리 대기 중
    while q:            # 큐가 비어있지 않으면
        i, j = q.pop(0)     # 디큐
        if maze[i][j]==3:   # 도착한 경우
            return visited[i][j] - 2    # 출발 도착을 제외한 경로의 길이 리턴
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0: # 인접-벽이 아니고, 인큐된적이 없으면
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

def dfs(i, j, N, c):
    global minV
    if maze[i][j]==3:
        if minV > c:
            minV = c
    else:
        visited[i][j] = 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                dfs(ni, nj, N, c+1)
        visited[i][j] = 0   # 다른 경로로 i,j에 진입하는 경우를 허용

def dfs2(i, j, N):
    if maze[i][j]==3:
        return 1
    else:
        visited[i][j] = 1
        ans = -1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                r = dfs2(ni, nj, N)
                if r:
                    if ans==-1:
                        ans = r
                    else:
                        ans = min(ans, r)
        visited[i][j] = 0   # 다른 경로로 i,j에 진입하는 경우를 허용
        return ans+1

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                return i, j
    # return -1, -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    # r = bfs(sti, stj, N)
    # print(f'#{tc} {r}')
    # dfs인 경우
    visited = [[0]*N for _ in range(N)]
    # minV = N*N
    # dfs(sti, stj, N, 0)
    # if minV == N*N: # 도착을 못한경우
    #     minV = 1
    # print(f'#{tc} {minV-1}')    # 경로길이에서 도착지 제외
    r = dfs2(sti, stj, N)       # 리턴값을 사용하는 dfs
    if r>0:
        r -= 2
    print(f'#{tc} {r}')