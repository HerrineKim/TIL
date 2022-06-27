def DFS(n, ci, cj, num):
    if n == 7:
        sset.add(num)
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(n + 1, ni, nj, num * 10 + arr[ni][nj])


T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    print(f'#{test_case} {len(sset)}')
