def dijkstra(s, V):
    U = [0]*(V+1)       # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정
    D[s] = 0
    for v, w in adjL[s]:
        D[v] = w

    # 남은 정점의 비용 결정
    for _ in range(V):      # 남은 정점 개수만큼 반복
        # D[t]가 최소인 t 결정, 비용이 결정되지 않은 정점t 중에서
        minV = INF
        t = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        U[t] = 1                # 비용 결정
        for v, w in adjL[t]:
                D[v] = min(D[v], D[t]+w)

INF = 10000
V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjL[u].append([v, w])

D = [INF]*(V+1)
dijkstra(0, V)
print(D)