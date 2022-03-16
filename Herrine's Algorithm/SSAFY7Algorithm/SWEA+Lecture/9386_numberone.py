T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input()))
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if nums[i] == 1:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f'#{test_case} {max_cnt}')
