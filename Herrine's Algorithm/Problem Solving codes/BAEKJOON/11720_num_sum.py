# 11720 숫자의 합
N = int(input())  # N 숫자의 개수
nums = list(input())
ans = 0
for i in range(N):
    ans += int(nums[i])
print(ans)