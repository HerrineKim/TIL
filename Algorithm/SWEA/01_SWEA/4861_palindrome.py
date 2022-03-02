T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0 for _ in range(N)]  # 0으로 이루어진 면적 동일한 격자판 생성
    for x in range(N):
        arr[x] = list(input())
    cnt = 0
    print(f'#{test_case}', end=' ')

    for i in range(N):  # 행탐색
        for j in range(0, N - M + 1):
            for k in range(M // 2):  # 회문인지 체크하고, 절반 길이만큼 cnt에 담아줌
                if arr[i][j + k] == arr[i][j + M - k - 1]:
                    cnt += 1
            if cnt == M // 2:  # 만약 cnt가 우리가 찾는 회문 길이 // 2 이면
                for l in range(j, j + M):  # 해당 회문 원하는 회문 길이에 맞추어 출력해 줌
                    print(arr[i][l], end=' ')
            cnt = 0

    cnt = 0
    for j in range(N):  # 열탐색. 행탐색과 동일한 과정이며 행에 없다면 열에서 찾아서 출력하게 되는 것
        for i in range(0, N - M + 1):
            for k in range(M // 2):
                if arr[i + k][j] == arr[i + M - k - 1][j]:
                    cnt += 1
            if cnt == M // 2:
                for l in range(i, i + M):
                    print(arr[l][j], end=' ')
            cnt = 0
    print('')
