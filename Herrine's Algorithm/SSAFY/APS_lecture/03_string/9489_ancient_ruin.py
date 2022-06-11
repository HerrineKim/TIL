# 9489. 고대 유적
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N = 행  M = 열
    arr = [list(map(int, input().split())) for _ in range(N)]  # 격자판
    cnt = 0

    max_cnt_row = 0
    max_cnt_col = 0
    for i in range(N):  # 행들 조사
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if cnt >= max_cnt_row:
                    max_cnt_row = cnt
            else:
                cnt = 0
    cnt = 0
    for j in range(M):  # 열들 조사
        for i in range(N):
            if arr[i][j]:
                cnt += 1
                if cnt >= max_cnt_col:
                    max_cnt_col = cnt
            else:
                cnt = 0

    max_result = 0
    if max_cnt_col <= max_cnt_row:
        max_result = max_cnt_row
    else:
        max_result = max_cnt_col
    print(f'#{test_case} {max_result}')

'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1

#1 3
#2 3
#3 6
'''