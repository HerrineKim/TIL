def bfs(x, y, N, M):
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        (i, j) = q.pop(0)
        # print((i, j))
        if (i, j) == (N-1, M-1):
            return visited[i][j]
        for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

N, M = map(int, input().split())
matrix = [list(map(int,input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
# destination = (N-1, M-1)
res = bfs(0, 0, N, M)
print(res)


# print(matrix)
