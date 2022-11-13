# 5097. 회전
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N 숫자의 개수 M 작업 횟수
    nums = list(map(int, input().split()))  # 숫자들 리스트
    M %= N
    res = nums[M]
    print(f'#{test_case} {res}')