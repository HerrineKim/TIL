'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):
    q = []  # 큐샐성
    visited = [0] * (V + 1)  # vistied생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 인큐표시
    while q:
        v = q.pop(0)  # 디큐
        print(v, end=' ')
        for w in range(1, V + 1):
            if adjM[v][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return


def bfs2(s, V):
    q = []  # 큐샐성
    visited = [0] * (V + 1)  # vistied생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 인큐표시
    while q:
        v = q.pop(0)  # 디큐
        print(v, end=' ')
        for w in adjL[v]:  # 인접리스트
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    # adjM[n2][n1] = 1

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V)
print()
bfs2(1, V)
print()
