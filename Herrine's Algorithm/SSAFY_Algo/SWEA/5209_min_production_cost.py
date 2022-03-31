# 5209. 최소생산비용
# dfs 백트래킹 기본 형식을 묻는 문제
def dfs(idx, visited, res):
    global maxV
    # 종료조건 & 백트래킹
    if idx == N:
        maxV = min(maxV, res)
        return
    if res >= maxV:
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            dfs(idx + 1, visited, res + arr[idx][i])
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N 제품 & 공장의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 99 * N * N
    v = []
    dfs(0, v, 0)
    print(f'#{tc} {maxV}')
