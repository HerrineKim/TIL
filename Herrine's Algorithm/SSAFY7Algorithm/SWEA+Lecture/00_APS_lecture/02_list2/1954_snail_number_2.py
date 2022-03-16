# 교수님 코드
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    d = 1
    i = 0  # 숫자를 기록할 위치 i, j
    j = 0  #
    k = 0  # 진행방향
    while d <= N * N:  # 쓸 숫자가 남아있으면
        if 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
            arr[i][j] = d
            i, j = i + di[k], j + dj[k]
            d += 1
        else:  # 숫자를 쓸 수 없는 경우
            i, j = i - di[k], j - dj[k]  # 이전 칸에서
            k = (k + 1) % 4  # 방향바꾸기(우회전)
            i, j = i + di[k], j + dj[k]  # 새로운 방향으로 다음 칸 인덱스
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
