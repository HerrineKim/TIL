import sys
sys.setrecursionlimit(10 ** 6)

n, m, r= map(int, sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

visited =[0]*(n+1)

cnt=1
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i ,visited)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):
    graph[i].sort()

dfs(graph, r ,visited)

for i in range(1, n + 1):
    print(visited[i])