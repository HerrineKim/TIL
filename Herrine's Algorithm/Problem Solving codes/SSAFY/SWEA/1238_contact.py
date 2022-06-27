import sys
sys.stdin = open("input_01.txt", "r")


def BFS(s):
    q = []
    v = [0]*101

    q.append(s)
    v[s] = 1
    sol = s

    while q:
        c = q.pop(0)
        if v[sol] < v[c] or v[sol] == v[c] and sol < c:
            sol = c
        for j in range(1, 101):
            if adj[c][j] and v[j] == 0:
                q.append(j)
                v[j] = v[c] + 1
    return sol


T = 1
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] Lst 연결 값을 인접 행렬에 저장
    adj = [[0]*101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1
    ans = BFS(S)
    print(f'#{test_case} {ans}')
