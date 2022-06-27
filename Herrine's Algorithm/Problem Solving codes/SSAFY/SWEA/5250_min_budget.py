# 5250. 최소 비용
def f(A, N):
    v = [[1000000] * N for _ in range(N)]
    q = [(0, 0)]
    v[0][0] = 0  # 출발위치
    while q:  # 비용이 갱신되는 칸이 있으면
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = arr[ni][nj] - arr[i][j] if arr[ni][nj] > arr[i][j] else 0  # 높이 차에 의한 비용
                # 갱신 조건
                if v[ni][nj] > v[i][j] + diff + 1:  # 인접하고 비용이 갱신되면 인큐
                    v[ni][nj] = v[i][j] + diff + 1
                    q.append((ni, nj))  # 인접한 칸의 비용도 갱신 가능성이 있으므로
    return v[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    f(arr, N)