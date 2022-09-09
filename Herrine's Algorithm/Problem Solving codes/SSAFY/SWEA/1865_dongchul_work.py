def DFS(idx, temp):
    global res
    if temp <= res:
        return
    if idx == N and temp > res:
        res = temp
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            DFS(idx+1, temp * arr[idx][i]/100)
            v[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    v = [0] * N
    DFS(0, 1)
    print(f'#{tc} {res * 100:6f}')