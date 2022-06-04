d = [[1,0], [-1,0], [0,-1], [0,1]]
def find(x, y):
    cnt = 0
    stack = [(x, y)]
    m = arr[x][y]

    while stack:
        i, j = stack.pop()
        cnt += 1
        visited[i][j] = 1
        if arr[i][j] > m:
            m = arr[i][j]
        for di, dj in d:
            ni, nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<M and  arr[ni][nj] != 0 and visited[ni][nj] == 0:
                stack.append((ni,nj))
    return (cnt, m)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    ans_list = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                ans_list.append(find(i,j))


    sorted_ans_list = sorted(ans_list, key=lambda x : x[1], reverse=True)
    for i in range(len(sorted_ans_list)):
        print(sorted_ans_list[i][0], end=' ')