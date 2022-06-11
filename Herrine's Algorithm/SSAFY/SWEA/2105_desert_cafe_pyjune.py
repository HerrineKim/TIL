def f(i, j, si, sj, d, c, N):  # si, sj 출발칸, d 진행방향, c i,j까지 먹은 디저트 수
    global maxV
    if c > 0 and i == si and j == sj:  # 탐색 후 출발지로 되돌아 온 경우
        if maxV < c:
            maxV = c
    elif menu[cafe[i][j]]:  # 이미 먹은 음식이면
        return
    elif i < si:  # i+j < si+sj:     # 출발점으로 돌아갈 수 없는 경우
        return
    else:
        menu[cafe[i][j]] = 1  # 먹은 음식 추가

        # 90도, 단 출발지 제외. 출발지는 0번 방향으로만
        if d < 3:
            ni, nj = i + di[d + 1], j + dj[d + 1]
            if 0 <= ni < N and 0 <= nj < N and c > 0:
                f(ni, nj, si, sj, d + 1, c + 1, N)
        # 직진
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            f(ni, nj, si, sj, d, c + 1, N)
        menu[cafe[i][j]] = 0  # 이전 카페에서 재출발


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    maxV = -1
    menu = [0] * 101  # 메뉴 1~100번

    for i in range(N):
        for j in range(N):
            f(i, j, i, j, 0, 0, N)
    print(f'#{tc} {maxV}')
