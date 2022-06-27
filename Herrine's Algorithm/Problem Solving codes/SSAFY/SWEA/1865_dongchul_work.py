# 1865. 동철이의 일 분배
# 5209. 최소생산비용 문제와 같이 한 줄에 하나씩만 방문해야 하는 dfs 백트래킹 문제
def dfs(idx, ssum):
    global res
    if ssum <= res:
        return
    if idx == N and ssum > res:
        res = ssum
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, ssum * arr[idx][i] * 0.01)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res = 0 + 0 + 0  # 최소 확률로 초기화
    dfs(0, 1)
    print(f'#{tc} {res*100:6f}')