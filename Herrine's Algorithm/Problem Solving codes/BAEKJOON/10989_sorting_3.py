# 10989 수 정렬하기 3
MAX_NUM = 1000
nums = []
N = int(input())
for i in range(N):
    nums.append(int(input()))

# counting sort
count = [0] * (MAX_NUM + 1)
countSum = [0] * (MAX_NUM + 1)

for i in range(0, N):
    count[nums[i]] += 1

countSum[0] = count[0]

for i in range(1, MAX_NUM + 1):
    countSum[i] = countSum[i - 1] + count[i]

result = [0] * (N + 1)

for i in range(N-1, -1, -1):
    result[countSum[nums[i]]] = nums[i]
    countSum[nums[i]] -= 1
    
ans = ''
for i in range(1, N + 1):
    ans += str(result[i]) + ' '
print(ans)