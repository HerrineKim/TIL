def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n > 3:  # 종료조건
        return
    if n == 3 and ci == si and cj == sj and ans < cnt:  # 정답 갱신
        ans = cnt
        return

    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            DFS(k, ni, nj, v+[arr[ni][nj]], cnt+1)


di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N):
        for sj in range(N):
            DFS(0, si, sj, [], 0)
    print(f'#{test_case} {ans}')
