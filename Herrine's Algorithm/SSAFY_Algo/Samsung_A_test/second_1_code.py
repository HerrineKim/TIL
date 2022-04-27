def bfs(i, j):
    global ans
    visited = [[0] * W for _ in range(H)]
    queue = []
    for x in range(H):
        for y in range(W):
            queue.append((x, y))
    cnt = 0
    mat_two = matrix
    while cnt < 3:
        if h // 2 == 0:  # 짝수인 경우
            for di, dj in [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [-1, -1]]:
                ni, nj = w + di, h + dj
                if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == 0:
                    visited[ni][nj] += 1
                    mat_two[ni][nj] += mat_two[w][h]
                    cnt += 1
                    if cnt == 3:
                        ans.append((mat_two[ni][nj]))
                        mat_two = matrix
        else:
            for di, dj in [[0, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]:
                ni, nj = w + di, h + dj
                if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == 0:
                    visited[ni][nj] += 1
                    mat_two[ni][nj] += mat_two[w][h]
                    cnt += 1
                    if cnt == 3:
                        ans.append((mat_two[ni][nj]))
                        mat_two = matrix
                        w, h = queue.pop(0)

    return
# def dfs(i, j):
#     global ans
#     global minV
#     stack = []
#     visited = [[0] * W for _ in range(H)]
#     while 1:
#         visited[i][j] = 1
#         if minV >= ans:
#             return
#         else:
#             minV = ans


T = int(input())
for tc in range(1, T+1):
    W, H = map(int, input().split())  # W 가로 H 세로
    matrix = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    # res = bfs(0, 0)
    bfs(0, 0)
    maxV = max(ans)
    final = maxV * maxV
    print(ans)
    print(f'#{tc} {final}')
