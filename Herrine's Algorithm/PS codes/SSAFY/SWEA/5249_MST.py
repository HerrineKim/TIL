# 5249. 최소신장트리
# Prim 알고리즘
def prim():
    res = 0
    u = 0  # 가중치가 최소인 정점
    distance[u] = 0
    for _ in range(V + 1):
        minV = 987654321
        for v in range(V + 1):
            if visited[v] == 0 and minV > distance[v]:
                minV = distance[v]
                u = v
        visited[u] = 1
        res += matrix[par[u]][u]
        # 인접 정점에 업데이트하기
        for v in range(V + 1):
            # 인접하고 방문 안하고 간선의 가중치 정점의 가중치를 비교
            if matrix[u][v] != 0 and visited[v] == 0 and matrix[u][v] < distance[v]:
                distance[v] = matrix[u][v]  # 가중치
                par[v] = u

    return res


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V 노드 E 간선
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    distance = [987654321] * (V + 1)
    par = list(range(V + 1))
    visited = [0] * (V + 1)
    for i in range(E):
        nnw = list(map(int, input().split()))  # n1 n2 w 노드 1 노드 2 가중치
        matrix[nnw[0]][nnw[1]] = nnw[2]
        matrix[nnw[1]][nnw[0]] = nnw[2]
    ans = prim()
    print(f"#{tc} {ans}")
