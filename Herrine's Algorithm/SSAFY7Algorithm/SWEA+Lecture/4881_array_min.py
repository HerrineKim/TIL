def f(i, N):
    global minV
    if i == N:
        s = 0
        for j in range(N):
            s += arr[j][p[j]]  # p[j] j번 행에서 고른 열 번호
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000
    p = [i for i in range(N)]  # p[i]: i번 행에서 고른 열의 번호
    f(0, N)

    print(f'#{tc} {minV}')