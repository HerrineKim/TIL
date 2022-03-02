T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    minN = nums[0]
    for i in range(1, N):
        if minN > nums[i]:
            minN = nums[i]
    print(f'#{tc} {nums.index(minN)+1}')
