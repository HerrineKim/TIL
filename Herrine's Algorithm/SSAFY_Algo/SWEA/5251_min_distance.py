# 5251. 최소이동거리
# dijkstra
def my_dijkstra(start):
    dist[start] = 0
    for _ in range(N+1):
        min_idx = -1
        min_V = 987654321
        for i in range(N+1):
            if not v[i] and dist[i] < min_V:
                min_idx = i
                min_V = dist[i]
        v[min_idx] = 1
        for j in range(N+1):
            if matrix[min_idx][j] and not v[j]:
                dist[j] = min(dist[j], dist[min_idx] + matrix[min_idx][j])


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N 연결 지점 개수 E 간선
    nnw = [list(map(int, input().split())) for _ in range(E)]  # n1 n2 w
    # 인접 행렬
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for n1, n2, w in nnw:
        matrix[n1][n2] = w
    v = [0] * (N + 1)
    dist = [98765431] * (N + 1)
    my_dijkstra(0)
    print(f'#{tc} {dist[N]}')
