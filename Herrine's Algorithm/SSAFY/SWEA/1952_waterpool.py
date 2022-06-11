def DFS(n, ssum):
    global ans
    if n > 12:
        if ans > ssum:
            ans = ssum
        return

    DFS(n+1, ssum + lst[n] * day)  # 일일권
    DFS(n+1, ssum + mon)  # 월간
    DFS(n+3, ssum + mon3)  # 분기
    DFS(n+12, ssum + year)  # 연간


T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    ans = 12345678
    DFS(1, 0)
    print(f'#{test_case} {ans}')