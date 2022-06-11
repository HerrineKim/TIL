# 4861. hwemun
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    strs = [list(input())for _ in range(N)]  # 격자판

    # 행 체크
    for i in range(N):
        for j in range(N - M + 1):
            temp1 = []
            temp2 = []
            for k in range(M):  # 길이 만큼의 문자열들 담아 주기
                temp1.append(strs[i][j+k])
            temp2.append(temp1[::-1])  # 뒤집기
            if temp2[0] == temp1:  # 문자열과 뒤집어진 문자열 회문 여부 비교
                print(f'#{test_case}', end=' ')
                print(''.join(temp2[0]))

    # 없었다면 열 체크
    for i in range(N):
        for j in range(N - M + 1):
            temp1 = []
            temp2 = []
            for k in range(M):
                temp1.append(strs[j+k][i])
            temp2.append(temp1[::-1])
            if temp2[0] == temp1:
                print(f'#{test_case}', end=' ')
                print(''.join(temp2[0]))

