# 파리 퇴치

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    cnt += arr[ii][jj]
            if sol < cnt:
                sol = cnt
    print(f'#{test_case} {sol}')
