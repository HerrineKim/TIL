def f(i, N):
    global minV
    if i == N:    # 모든행에서 열 선택 완료
        s = 0   # 선택한 원소의 합
        for j in range(N):
            s += arr[j][p[j]] # p[j] j번 행에서 고른 열 번호
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]


def f2(i, N, s):    # s : i-1행까지 선택한 원소의 합
    global minV
    if i == N:    # 모든행에서 열 선택 완료
        if minV > s:
            minV = s
    elif s >= minV:  # 선택한 원소의 합이 최소값 이상이면
        return      # 중단하고 이전 행으로 돌아가서 다른 원소 선택
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f2(i+1, N, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000
    p = [i for i in range(N)]   # p[i] : i번 행에서 고른 열의 번호
    f(0, N)
    print(f'#{tc} {minV}')
