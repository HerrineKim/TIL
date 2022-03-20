# 5105. 미로의 거리
# bfs
def bfs(si, sj, ei, ej):
    q = []
    visited = [[0] * N for _ in range(N)]

    q.append(([si, sj]))  # Q에 초기데이터들 삽입, 방문표시
    visited[si][sj] = 1  # 출발점에 방문 표시

    while q:
        ci, cj = q.pop(0)  # 큐에서 출발점을 pop
        if ci == ei and cj == ej:  # 만약 방문한 곳이 끝 점과 같다면 종료
            return visited[ci][cj] - 2 # 현재 visited 값에서 시작점과 종료 지점을 뺀 값 return
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):  # 사방탐색
            ni, nj = ci + di, cj + dj
            # 만약 계속 탐색해나갈 수 있는 지점이라면 큐에 append
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] and MAP[ni][nj] != '1':
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1  # append 한 후에는 지나온 거리 + 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '2':  # 출발 지점 찾기
                si, sj = i, j
            elif MAP[i][j] == '3':  # 도착 지점 찾기
                ei, ej = i, j

    sol = bfs(si, sj, ei, ej)  # 최소 칸 수를 return 해주는 bfs 함수
    print(f'#{test_case} {sol}')
