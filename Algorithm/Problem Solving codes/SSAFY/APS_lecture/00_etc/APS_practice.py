pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1],
        [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]] 
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
opp = [2, 3, 0, 1]

def BFS(N, M, si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)]
    
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1
    
    while q:
        ci, cj  = q.pop(0)
        