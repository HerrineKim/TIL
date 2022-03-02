T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 당근의 개수
    nums = list(map(int, input().split()))  # 모든 당근들의 수
    cnt = max_cnt = 1  # 구간의 최소 길이 1
    for i in range(1, N):  # count가 1부터 시작하기 때문에 1에서 시작
        if nums[i-1] < nums[i]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{test_case} {max_cnt}')
