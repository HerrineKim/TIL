# 1978. 소수 찾기
N = int(input())
nums = list(map(int, input().split()))
ans = []

for i in range(N):
    cnt = 0
    for j in range(1, nums[i] + 1):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 2:
        ans.append(nums[i])

print(len(ans))
