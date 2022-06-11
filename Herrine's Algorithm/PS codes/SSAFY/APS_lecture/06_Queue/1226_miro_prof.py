def dfs(i, j):
    if maze[i][j]==3:
        return 1
    else:
        maze[i][j] = 1      # 진입한 칸을 벽으로 메꿈
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj]!=1:   # 벽으로 둘러쌓인 경우 범위검사 생략
                if dfs(ni, nj):     # ni, nj로 이동 후 리턴시 1 또는 0을 받음
                    return  1       # 리턴값 1을 받은경우 탐색 성공. 1리턴
        return 0    # 현재 칸으로부터 이동 후 도착점을 찾지 못하면

def dfs_stack(i,j):
    stack = []
    visited = [[0]*16 for _ in range(16)]
    stack.append((i,j)) # 시작점 push
    visited[i][j] = 1   # 갈림길 목록에 포함된 칸임을 표시
    while stack:    # 스택이 비어있지 않으면(갈림길이 남아있으면)
        i, j = stack.pop()
        if maze[i][j]==3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj]!=1 and visited[ni][nj]==0:
                stack.append((ni,nj))
                visited[ni][nj] = 1
    return 0    # 도착 못한 경우

def bfs(i,j):
    q = []
    visited = [[0]*16 for _ in range(16)]
    q.append((i,j)) # 시작점 push
    visited[i][j] = 1   # 갈림길 목록에 포함된 칸임을 표시
    while q:    # 스택이 비어있지 않으면(갈림길이 남아있으면)
        i, j = q.pop(0)
        if maze[i][j]==3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = 1
    return 0    # 도착 못한 경우

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                return i, j

for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)] # 배열에 숫자로 저장 -> 지나간 칸을 벽으로
    sti, stj = find_start()     # 시작위치
    #r = dfs(sti, stj)           # 도착하면 1, 못하면 0
    #r = dfs_stack(sti, stj)
    r = bfs(sti, stj)
    print(f'#{tc} {r}')